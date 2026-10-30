const { chromium } = require('playwright');
const assert = require('node:assert/strict');
(async () => {
 const browser = await chromium.launch({channel:'chrome',headless:true});
 const page = await browser.newPage({viewport:{width:1280,height:900}});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto('http://localhost:8765');
 assert.equal(await page.locator('[data-roteiro]').count(),10);
 for(let n=1;n<=10;n++) {
   const id=String(n).padStart(2,'0');
   await page.locator('[data-roteiro="'+id+'"]').evaluate(e=>e.focus());
   await page.locator('[data-roteiro="'+id+'"]').click();
   await page.waitForFunction(()=>document.querySelector('#roteiroContent').getAttribute('aria-busy')==='false');
   assert(await page.locator('#roteiroContent h1').count());
   assert((await page.locator('#roteiroContent').innerText()).length>3000);
   const pdf=await page.request.get(await page.locator('#roteiroDownload').getAttribute('href'));
   assert(pdf.ok());assert((await pdf.body()).subarray(0,5).toString()==='%PDF-');
   await page.keyboard.press('Escape');
   assert.equal(await page.locator('[data-roteiro="'+id+'"]').evaluate(e=>e===document.activeElement),true);
 }
 await page.setViewportSize({width:390,height:844});
 await page.locator('[data-roteiro="10"]').evaluate(e=>e.focus());
 await page.locator('[data-roteiro="10"]').click();
 await page.waitForFunction(()=>document.querySelector('#roteiroContent').getAttribute('aria-busy')==='false');
 assert(await page.locator('#roteiroDownload').isVisible());
 assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
 await page.screenshot({path:'tmp-mobile.png'});
 await page.locator('#roteiroClose').focus();await page.keyboard.press('Tab');
 assert.equal(await page.evaluate(()=>document.activeElement.id),'roteiroContent');
 await page.keyboard.press('Tab');assert.equal(await page.evaluate(()=>document.activeElement.id),'roteiroDownload');
 await page.mouse.click(2,2);assert.equal(await page.locator('#roteiroDialog').evaluate(e=>e.open),false);
 assert.deepEqual(errors,[]);
 console.log('PASS: 10 modal previews, 10 real PDFs, Escape/focus restoration, Tab trap, backdrop close, 390px layout; no JS errors');
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
