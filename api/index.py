import os
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
        path = parsed.path.rstrip('/')
        params = urllib.parse.parse_qs(parsed.query)

        # 0. Lokal rejimda kompyuterda ochilganda HTML sahifani qaytarish
        if path in ['', '/index.html']:
            html_path = os.path.join(os.path.dirname(__file__), '..', 'public', 'index.html')
            if os.path.exists(html_path):
                with open(html_path, 'r', encoding='utf-8') as f:
                    content = f.read().encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(content)
                return

        # 1. Health check tekshiruvi
        if path.endswith('/health'):
            self.send_json(200, {
                'status': 'healthy',
                'server': 'Vercel Serverless (Python 3.12)',
                'xabar': 'Bulut infratuzilmasi barqaror ishlamoqda.'
            })
            return

        # 2. Hisoblash (agar /add bo'lsa yoki parametrda a va b kelsa)
        if path.endswith('/add') or ('a' in params and 'b' in params):
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
                return

            except ValueError:
                self.send_json(400, {
                    'status': 'error',
                    'xato': 'Iltimos, faqat haqiqiy sonlar kiriting!'
                })
                return
            except Exception as e:
                self.send_json(500, {
                    'status': 'error',
                    'xato': str(e)
                })
                return

        # 3. Asosiy API statusi
        self.send_json(200, {
            'status': 'online',
            'xizmat': 'Bulutli Texnologiyalar CI/CD Serverless API',
            'versiya': '1.1.0',
            'endpoints': {
                'hisoblash': '/api/add?a=25&b=75&amal=+',
                'salomatlik': '/api/health'
            }
        })

if __name__ == '__main__':
    from http.server import HTTPServer
    import webbrowser
    port = 5000
    print(f"Lokal server ishga tushdi: http://localhost:{port}")
    try:
        webbrowser.open(f"http://localhost:{port}")
    except Exception:
        pass
    httpd = HTTPServer(('127.0.0.1', port), handler)
    httpd.serve_forever()
