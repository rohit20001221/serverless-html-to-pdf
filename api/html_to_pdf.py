from http.server import BaseHTTPRequestHandler
from xhtml2pdf import pisa
from io import StringIO, BytesIO

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/pdf')
        self.end_headers()

        html = "<h1>hello world</h1>"
        pdf = BytesIO()
        pisa.CreatePDF(html, pdf)
        data = pdf.getvalue()
        self.wfile.write(data)

        return