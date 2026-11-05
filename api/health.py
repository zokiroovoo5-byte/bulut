import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        resp_data = {
            'status': 'healthy',
            'server': 'Vercel Serverless (Python 3.12)',
            'xabar': 'Bulut infratuzilmasi barqaror ishlamoqda.'
        }
        payload = json.dumps(resp_data).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(payload)
