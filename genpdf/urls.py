from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from pyhtml2pdf import converter

def generate_pdf(request):
    target = "proposals/output.pdf"
    pdf_data = converter.convert('http://127.0.0.1:8000/view/', target, print_options={"scale": 0.95})
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=output.pdf'
    response['Content-Disposition'] = 'inline; filename=output.pdf'
    return response

def view_pdf(request):
    return render(request,"PROPOSAL_TEMPLATE4.html",{})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gen/', generate_pdf),
    path('view/', view_pdf),
]
