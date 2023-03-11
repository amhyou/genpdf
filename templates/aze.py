from weasyprint import HTML

# Define the path to your HTML file
html_path = 'index.html'

# Define the path to your output PDF file
pdf_path = 'index.pdf'

# Load the HTML file and generate the PDF
HTML(html_path).write_pdf(pdf_path)