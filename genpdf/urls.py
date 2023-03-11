from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
import subprocess

def generate_pdf(request):
    subprocess.check_call(['node', 'genpdf/genpdf.js'])
    with open('proposals/output.pdf', 'rb') as f:
        pdf_data = f.read()
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=output.pdf'
    return response

def view_pdf(request):
    return render(request,"PROPOSAL_TEMPLATE4.html",{})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gen/', generate_pdf),
    path('view/', view_pdf),
]
