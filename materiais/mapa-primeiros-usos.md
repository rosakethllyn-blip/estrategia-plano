# Aula 01 — IA do Zero: da conversa à criação

**Material de apoio • Estrateg[IA]**

## Mapa mental: 8 conceitos

1. **IA generativa**: sistemas capazes de gerar texto, imagem, código e outros conteúdos a partir de solicitações.
2. **Modelo**: componente que interpreta o contexto e produz a resposta.
3. **Aplicativo**: interface na qual você utiliza modelos e ferramentas, como ChatGPT ou Claude.
4. **Token**: unidade de processamento de linguagem, não necessariamente uma palavra.
5. **Contexto**: dados e instruções disponíveis para a resposta naquela interação.
6. **Ferramenta**: recurso que permite buscar informações ou executar uma ação autorizada.
7. **Agente**: sistema que pode trabalhar em ciclos de objetivo, plano, ações e verificação, dependendo de ferramentas, permissões e supervisão.
8. **Skill / conector / plugin / MCP**: mecanismos distintos para reutilizar procedimentos e dar acesso controlado a recursos e sistemas externos.

## PROMPT 01 — construir protótipo interativo (dados 100% fictícios)

```text
Quero que você atue como uma pessoa desenvolvedora de interfaces educacionais e me ajude a CRIAR um protótipo interativo, sem usar dados reais.

PROJETO: Painel demonstrativo de uma instituição de saúde fictícia, chamado “Painel de Gestão”.
PÚBLICO: coordenadores e gestores da saúde que nunca programaram.

REQUISITOS:
1. Entregue UM arquivo HTML completo, com CSS e JavaScript dentro do próprio arquivo, sem bibliotecas ou links externos.
2. Visual claro e profissional: fundo branco, texto quase preto, cor laranja #F23C00 para destaques, fonte de sistema e espaços de respiro.
3. Mostre três indicadores DIDÁTICOS E FICTÍCIOS: treinamentos concluídos 72%, atividades planejadas 18 e pendências 5. Informe visivelmente que são dados de demonstração.
4. Adicione uma lista de quatro atividades fictícias, cada uma com título, responsável “A definir”, status e um botão para marcar visualmente como concluída.
5. Adicione filtro para exibir todas, pendentes ou concluídas.
6. Crie um pequeno quadro “O que revisar antes de usar em uma instituição”, com alerta sobre dados, validação humana e necessidade de integração segura.
7. A interface deve funcionar em celular e computador.
8. Inclua comentários no código explicando de forma simples as partes principais.

IMPORTANTE:
- Não use servidores, banco de dados, login, APIs ou envio de dados.
- Não afirme que o protótipo já está conectado a qualquer sistema hospitalar.
- Ao atualizar o status, deixe claro que a mudança acontece só na página aberta e não é salva.
- Se a plataforma permitir gerar um arquivo, forneça o HTML. Se não, apresente o código completo em um único bloco ```html para que eu possa copiar e salvar como painel.html.

Antes de começar o código, resuma em 4 linhas o que você vai construir.
```

## PROMPT 02 — revisar e testar

```text
Revise o protótipo HTML que você acabou de criar.
1. Verifique se todos os botões realmente funcionam e se o filtro separa corretamente atividades pendentes e concluídas.
2. Confira se nenhum dado fictício foi apresentado como indicador real.
3. Confira acessibilidade básica: contraste, rótulos dos botões, foco de teclado e leitura em celular.
4. Se houver problemas, entregue o HTML COMPLETO corrigido, preservando a aparência.
5. Explique em linguagem simples o que você corrigiu e quais limitações permanecem: sem banco de dados, sem login, sem dados reais e sem integração com sistemas.
```

## Antes de compartilhar com alguém

- O protótipo usa números inventados só para aprendizagem.
- Clicar em “concluído” na página não altera a realidade de uma instituição.
- Uma versão de demonstração sem banco de dados ou login não é sistema de produção.
- Não use nomes de pacientes, dados clínicos, documentos protegidos ou informações internas sem autorização e controles institucionais.
- Revise código e resultados. Em um sistema real, há requisitos adicionais de segurança, acessibilidade, manutenção, auditoria e LGPD.

## Fontes

- Primeira aula do Ruan Braz, referência de estrutura didática: https://www.youtube.com/watch?v=P3PSw-mhPDM
- Projetos do ChatGPT: https://help.openai.com/pt-br/articles/10169521-projects-in-chatgpt
- Recursos do Claude Code Desktop: https://code.claude.com/docs/pt/desktop
- Glossário Estrateg[IA]: https://rosakethllyn-blip.github.io/modo-ia-saude-glossario/
