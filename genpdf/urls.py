from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

import subprocess
def generate_pdf(request):
    subprocess.check_call(['node', 'genpdf/pdf_by_pupeteer.js'])
    with open('output.pdf', 'rb') as f:
        pdf_data = f.read()
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=output.pdf'
    return response
    # get the HTML template
    template = get_template('PROPOSAL_TEMPLATE4.html')
    html = template.render()

    # create a PDF from the HTML
    pdf_file = BytesIO()
    pisa.CreatePDF(BytesIO(html.encode()), pdf_file)

    # create a Django response with the PDF file
    response = HttpResponse(pdf_file.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="my_pdf.pdf"'

    return response

def view_pdf(request):
    return render(request,"PROPOSAL_TEMPLATE4.html",{})

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,io
import time
from django.http import FileResponse
#from xvfbwrapper import Xvfb
def download_pdf(request):
    # Replace <download-directory> with the directory where you want to save the downloaded file
    if os.name == 'nt': # for Windows
        default_download_folder = os.path.join(os.environ['USERPROFILE'], 'Downloads')
        import win32api
        from win32process import CREATE_NEW_CONSOLE, CREATE_NO_WINDOW, DETACHED_PROCESS

        def start_xvfb():
            return None

        def stop_xvfb(display):
            pass
    elif os.name == 'posix': # for Linux and macOS
        default_download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    display = start_xvfb()
    chrome_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    chrome_capabilities['goog:chromeOptions'] = {
        'args': ['--no-sandbox']
    }
    chrome_capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}

    #with Xvfb() as xvfb:
    # Replace <path-to-chromedriver> with the actual path to the downloaded chromedriver executable
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome("chromedriver.exe",options=options,desired_capabilities=chrome_capabilities)
    driver.get("http://127.0.0.1:8000/view/")

    filename = 'file.pdf'
    file_path = os.path.join(default_download_folder, filename)

    while not os.path.exists(file_path):
        time.sleep(1) # wait for file to download
    driver.quit()

    stop_xvfb(display)

    with open(file_path, 'rb') as f:
        pdf_contents = f.read()
    pdf_file = io.BytesIO(pdf_contents)

    response = FileResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    return response

from selenium import webdriver
#import pdfkit
#import weasyprint
def download_pdf2(request):
    # Create the Chrome WebDriver instance
    driver = webdriver.Chrome()

    # Navigate to the page and render it
    driver.get('http://127.0.0.1:8000/view/')

    # Get the HTML content of the page
    html_content = driver.page_source

    # Use weasyprint to convert the HTML content to a PDF file
    pdf_file = weasyprint.HTML(string=html_content).write_pdf()

    # Save the PDF file to disk
    with open('page.pdf', 'wb') as f:
        f.write(pdf_file)

    # Quit the WebDriver instance
    driver.quit()

    return HttpResponse("fait")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gen/', generate_pdf),
    path('view/', view_pdf),
    path('download/', download_pdf),
    path('down/', download_pdf2),
]
