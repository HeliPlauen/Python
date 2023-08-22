
import http.server 


PORT = 8080

class CustomHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

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
        decoded_data = data.decode()        
        print(f"WE RECEIVED: {decoded_data}")
        MESSAGE_RESPONSE = f"RESPONSE FROM PORT {PORT} - OK!"
        self.wfile.write(bytes(MESSAGE_RESPONSE, "utf-8"))

        print("-----------------------------------------------------")


server_address = ('', PORT)
httpd = http.server.HTTPServer(server_address, CustomHTTPRequestHandler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()

