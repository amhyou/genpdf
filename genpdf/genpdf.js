const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: [
      '--disable-gpu'
    ]
  });
  const page = await browser.newPage();
  await page.goto('http://127.0.0.1:8000/view/');
  // await page.waitForNavigation({ waitUntil: 'networkidle0' });
  await page.pdf({ path: 'proposals/output.pdf', format: 'A4' });
  // const pdfBuffer = await page.pdf({ format: 'A4' });
  // fs.writeFileSync('output.pdf', pdfBuffer);
  await browser.close();
})();