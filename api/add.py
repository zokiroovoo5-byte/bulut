import json
import urllib.parse
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def send_json(self, status_code, data):
        payload = json.dumps(data).encode('utf-8')
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(payload)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        try:
            a_str = params.get('a', ['0'])[0]
            b_str = params.get('b', ['0'])[0]
            amal = params.get('amal', ['+'])[0]

            a = float(a_str)
            b = float(b_str)

            if amal in ['+', ' ', '']:
                amal = '+'
                natija = a + b
            elif amal == '-':
                natija = a - b
            elif amal == '*':
                natija = a * b
            elif amal == '/':
                if b == 0:
                    self.send_json(400, {
                        'status': 'error',
                        'xato': 'Nolga bo‘lish mumkin emas (Division by Zero)!'
                    })
                    return
                natija = round(a / b, 4)
            else:
                amal = '+'
                natija = a + b

            self.send_json(200, {
                'status': 'success',
                'a': a,
                'b': b,
                'amal': amal,
                'natija': natija,
                'bulut_provayder': 'Vercel Serverless Function',
                'dasturlash_tili': 'Python 3.12',
                'ci_cd': 'GitHub -> Vercel Avtomatik Deploy'
            })

        except ValueError:
            self.send_json(400, {
                'status': 'error',
                'xato': 'Iltimos, faqat haqiqiy sonlar kiriting!'
            })
        except Exception as e:
            self.send_json(500, {
                'status': 'error',
                'xato': str(e)
            })
