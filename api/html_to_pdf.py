from http.server import BaseHTTPRequestHandler
from urllib import parse
import pdfkit

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/pdf')
        self.end_headers()

        html = "<h1>hello world</h1>"
        pdf = pdfkit.from_string(html, False)
        data = pdf.to_bytes()
        self.wfile.write(data)

        return