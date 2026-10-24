"""
================================================================================
CHIT FUND TRACKER - MULTI-DEVICE WI-FI SERVER & LIVE SYNC ENGINE
================================================================================
Purpose:
  1. Serves the Chit Fund Manager web app to Mobile Phones, Tablets, and PCs
     over local Wi-Fi.
  2. Provides a zero-dependency JSON sync API (`/api/sync`) so edits on your
     Tablet or Phone instantly sync to this PC and vice versa.
  3. Uses ThreadingHTTPServer for fast, non-blocking concurrent requests.

NOTE:
  If you are only using this app on your PC, you do NOT even need to run this!
  You can simply double-click `index.html` directly in Chrome or Edge.
================================================================================
"""

import os
import json
import socket
from http.server import SimpleHTTPRequestHandler
try:
    from http.server import ThreadingHTTPServer
except ImportError:
    from http.server import HTTPServer as ThreadingHTTPServer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'chit_sync_data.json')
PORT = 8080


class ChitSyncHandler(SimpleHTTPRequestHandler):
    """Handles static web asset serving + lightweight JSON sync API."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def log_message(self, format, *args):
        try:
            super().log_message(format, *args)
        except Exception:
            pass

    def do_GET(self):
        # Real-time state read endpoint
        if self.path == '/api/sync':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.end_headers()

            if os.path.exists(DATA_FILE):
                try:
                    with open(DATA_FILE, 'r', encoding='utf-8') as f:
                        data = f.read()
                except Exception:
                    data = '{}'
            else:
                data = '{}'

            self.wfile.write(data.encode('utf-8'))
            return

        # Server health check
        elif self.path == '/api/ping':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'{"status":"ok"}')
            return

        super().do_GET()

    def do_POST(self):
        # Real-time state write endpoint
        if self.path == '/api/sync':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            try:
                parsed = json.loads(body)
                with open(DATA_FILE, 'w', encoding='utf-8') as f:
                    json.dump(parsed, f, indent=2, ensure_ascii=False)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(b'{"status":"saved"}')
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
            return

        super().do_POST()

    def do_OPTIONS(self):
        # CORS preflight support for cross-origin mobile browser fetch
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


def get_local_ip():
    """Detects local LAN IPv4 address for mobile access."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return '127.0.0.1'


def run_server():
    import sys
    try:
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    ip = get_local_ip()
    print('=' * 70)
    print('   CHIT FUND REALTIME SYNC SERVER (PHONE + TABLET + PC)')
    print('=' * 70)
    print(f' Local IP Address   : {ip}')
    print(f' Open on Phone / Tab: http://{ip}:{PORT}')
    print(f' Open on this PC    : http://localhost:{PORT}')
    print('-' * 70)
    print(' * Multi-threaded: Phone & PC work simultaneously without freezing.')
    print(' * All edits on Phone or Tab automatically sync here in real-time.')
    print(' * Press Ctrl + C to stop the server.')
    print('=' * 70)

    server = ThreadingHTTPServer(('0.0.0.0', PORT), ChitSyncHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n[INFO] Server gracefully stopped.')


if __name__ == '__main__':
    run_server()
