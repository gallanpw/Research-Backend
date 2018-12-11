from http.server import HTTPServer, BaseHTTPRequestHandler
import random
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':

            response = {
                'billing_id': 'deniansyah',
                'customer_id' : 'roni argantone',
                'location_id' : 'adi imam maulana',
            }
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(str.encode("Hello Python\n")))
            for x in range(10000):
                self.wfile.write(bytes(str.encode("Your Number : " + str(random.randint(0,1000)) + "\n")))
            return
        # return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self) 
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()