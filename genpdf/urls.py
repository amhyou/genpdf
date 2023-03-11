from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
import subprocess
'''
from django.template.loader import get_template
import asyncio
from pyppeteer import launch
async def generate():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://127.0.0.1:8000/view/')
    await page.pdf({ path: 'proposals/output.pdf', format: 'A4' })
    await browser.close()
# asyncio.get_event_loop().run_until_complete(generate())
'''
def generate_pdf(request):
    # await generate()
    subprocess.check_call(['node', 'genpdf/genpdf.js'])
    with open('proposals/output.pdf', 'rb') as f:
        pdf_data = f.read()
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=output.pdf'
    #response['Content-Disposition'] = 'inline; filename=output.pdf'
    return response

def view_pdf(request):
    return render(request,"PROPOSAL_TEMPLATE4.html",{})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gen/', generate_pdf),
    path('view/', view_pdf),
]
