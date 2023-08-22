
import json
import http.server as HTTP 


class CustomHTTPRequestHandler(HTTP.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET request received!!!")

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Simple HTTP-server.</title></head>'.encode())
        self.wfile.write('<body>The GET-request was received!</body></html>'.encode())

        print("-----------------------------------------------------")

    def do_POST(self):
        print("POST request received!!!")        

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.send_header('Server', 'ServerINFO')
        self.end_headers()        

        # Get data size
        content_length = int(self.headers['Content-Length'])

        # Get data itself
        data = self.rfile.read(content_length)    
        decoded_data = json.loads(data.decode())        
        print(f"WE RECEIVED: {decoded_data}")
        coded_data = decoded_data["key"].encode("utf-8")
        print(f"{coded_data} - type:{type(coded_data)}")
        self.wfile.write(coded_data)

        print("-----------------------------------------------------")

    def do_PUT(self):
        print("PUT request received!!!")        

        self.send_response(200)
        print("-----------------------------------------------------")

    def do_DELETE(self):
        print("DELETE request received!!!")        

        self.send_response(200)
        print("-----------------------------------------------------")


PORT = 9999
server_address = ('', PORT)
httpd = HTTP.HTTPServer(server_address, CustomHTTPRequestHandler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()

