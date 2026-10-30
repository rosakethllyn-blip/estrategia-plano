"""Build static, matching HTML previews and PDFs. pip install reportlab markdown pypdf"""
import re
import json
import html
from pathlib import Path
import xml.etree.ElementTree as ET
import markdown
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'roteiros' / 'pdf'
PREVIEW = ROOT / 'roteiros' / 'preview'
OUT.mkdir(exist_ok=True)
PREVIEW.mkdir(exist_ok=True)
FONT = Path('C:/Windows/Fonts')
pdfmetrics.registerFont(TTFont('Body', str(FONT / 'arial.ttf')))
pdfmetrics.registerFont(TTFont('Body-Bold', str(FONT / 'arialbd.ttf')))
pdfmetrics.registerFont(TTFont('Body-Italic', str(FONT / 'ariali.ttf')))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Body-Bold', italic='Body-Italic', boldItalic='Body-Bold')
styles = getSampleStyleSheet()
for name in ['Normal', 'BodyText', 'Heading1', 'Heading2', 'Heading3']:
    styles[name].fontName = 'Body'
    styles[name].fontSize = 10
    styles[name].leading = 15
    styles[name].spaceAfter = 9
styles['Heading1'].fontSize = 24
styles['Heading1'].leading = 30
styles['Heading2'].fontName = 'Body-Bold'
styles['Heading2'].fontSize = 13
styles['Heading2'].leading = 19
styles['Heading2'].textColor = colors.HexColor('#B92A0A')
styles['Heading2'].spaceBefore = 20
styles.add(ParagraphStyle('Speech', parent=styles['BodyText'], leftIndent=14, borderColor=colors.HexColor('#F23C00'), borderWidth=0, borderPadding=9, spaceBefore=5, spaceAfter=14))
styles.add(ParagraphStyle('Note', parent=styles['BodyText'], textColor=colors.HexColor('#57575B'), backColor=colors.HexColor('#F5F3F1'), borderPadding=8, spaceBefore=8, spaceAfter=14))
styles.add(ParagraphStyle('Cell', parent=styles['BodyText'], fontSize=8, leading=12, spaceAfter=0))
styles.add(ParagraphStyle('Cover', parent=styles['Heading1'], fontName='Body-Bold', fontSize=30, leading=38, spaceAfter=28))

def inline(el):
    s = html.escape(el.text or '')
    for child in el:
        tag = {'strong': 'b', 'em': 'i', 'code': 'font'}.get(child.tag, child.tag)
        attrs = ' name="Body"' if child.tag == 'code' else ''
        if tag == 'a':
            href = child.get('href', '')
            if href.startswith(('https://', 'http://')):
                attrs = ' href="' + html.escape(href, quote=True) + '" color="#B92A0A"'
            else:
                tag = 'span'
        s += '<' + tag + attrs + '>' + inline(child) + '</' + tag + '>' + html.escape(child.tail or '')
    return s

def blocks(parent, speech=False):
    result = []
    for el in parent:
        if el.tag in ('h1', 'h2', 'h3', 'h4'):
            # The full original heading remains in the body, even when editorial metadata differs.
            result.append(Paragraph(inline(el), styles['Heading2' if el.tag in ('h1', 'h2') else 'Heading3']))
        elif el.tag == 'blockquote':
            result.extend(blocks(el, True))
        elif el.tag == 'p':
            note = (el.text or '').strip() == '' and len(el) and el[0].tag == 'strong' and not speech
            result.append(Paragraph(inline(el), styles['Speech' if speech else 'Note' if note else 'BodyText']))
        elif el.tag in ('ul', 'ol'):
            for i, li in enumerate(el, 1):
                result.append(Paragraph(('• ' if el.tag == 'ul' else f'{i}. ') + inline(li), styles['BodyText']))
        elif el.tag == 'pre':
            for line in ''.join(el.itertext()).splitlines():
                result.append(Paragraph(html.escape(line) or ' ', styles['Note']))
        elif el.tag == 'table':
            rows = [[Paragraph(inline(cell), styles['Cell']) for cell in row] for row in el.findall('.//tr')]
            table = Table(rows, colWidths=[(475 / len(rows[0]))] * len(rows[0]), repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND', (0,0),(-1,0),colors.HexColor('#FCE7DF')),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),.4,colors.HexColor('#DDD8D4')),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
            result += [table, Spacer(1,12)]
        elif el.tag == 'hr':
            result.append(Spacer(1,12))
        else:
            raise ValueError(f'Unsupported block: {el.tag}')
    return result

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.saved = []
    def showPage(self):
        self.saved.append(dict(self.__dict__))
        self._startPage()
    def save(self):
        total = len(self.saved)
        for state in self.saved:
            self.__dict__.update(state)
            self.setStrokeColor(colors.HexColor('#F23C00'))
            self.line(60, 48, 535, 48)
            self.setFont('Body', 8)
            self.setFillColor(colors.HexColor('#57575B'))
            self.drawString(60, 34, 'MODO ESTRATEG[IA]  /  ROTEIRO DE GRAVAÇÃO')
            self.drawRightString(535, 34, f'{self._pageNumber} / {total}')
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

for ep in json.loads((ROOT / 'episodios.json').read_text(encoding='utf-8')):
    n = ep['n']
    source = (ROOT / 'roteiros' / ep['filename']).read_text(encoding='utf-8')
    body = re.sub(r'\A---\s*\n.*?\n---\s*\n', '', source, count=1, flags=re.S)
    rendered = markdown.markdown(body, extensions=['tables', 'fenced_code'])
    (PREVIEW / f'ep{n:02}.html').write_text(rendered, encoding='utf-8')
    tree = ET.fromstring('<article>' + rendered + '</article>')
    actual_title = ''.join(tree.find('h1').itertext())
    story = [Spacer(1,75), Paragraph('MODO ESTRATEG[IA]', styles['Heading2']), Spacer(1,25), Paragraph(f'ROTEIRO / EPISÓDIO {n:02}', styles['BodyText']), Spacer(1,18), Paragraph(html.escape(actual_title), styles['Cover']), Paragraph('Rosa Kethllyn', styles['Heading2']), Paragraph('Roteiro completo de gravação<br/>Cenas, falas e orientações de produção', styles['BodyText']), PageBreak()]
    story.extend(blocks(tree))
    doc = SimpleDocTemplate(str(OUT / f'ep{n:02}.pdf'), pagesize=(595.28,841.89), leftMargin=60, rightMargin=60, topMargin=55, bottomMargin=70, title=actual_title, author='Rosa Kethllyn / Modo Estrateg[IA]')
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f'EP{n:02}: preview and PDF built')
