from http.server import BaseHTTPRequestHandler
from xhtml2pdf import pisa
from io import StringIO, BytesIO

def getPdf(html):
    pdf = BytesIO()
    pisa.CreatePDF(StringIO(html), pdf)
    data = pdf.getvalue()

    return data

class handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type','application/pdf')
        self.end_headers()

    def do_GET(self):
        self._set_headers()

        html = "<h1>hello world</h1>"
        data = getPdf(html)
        self.wfile.write(data)

        return

    def do_POST(self):
        self._set_headers()

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        data = getPdf(post_body)
        self.wfile.write(data)