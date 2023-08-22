
import json
import http.server 
import urllib.request


PORT = 8888

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
        decoded_data = json.loads(data.decode()) 
        print(f"WE RECEIVED: {decoded_data}")
        
        ADDRESS_FOR_REQUEST = decoded_data["url"]
        PORT_FOR_REQUEST = decoded_data["port"]
        METHOD_FOR_REQUEST = decoded_data["method"]
        MESSAGE_REQUEST = f"MESSAGE FORM PORT {PORT} - OK!"
        MESSAGE_RESPONSE = f"RESPONSE FROM PORT {PORT} - OK!"

        rqst = urllib.request.Request(
            url=ADDRESS_FOR_REQUEST+":"+str(PORT_FOR_REQUEST),
            method=METHOD_FOR_REQUEST, data=bytes(MESSAGE_REQUEST, "utf-8")
        )
        with urllib.request.urlopen(rqst) as f:
            print(f.getcode())
            print(f.msg)
            print(f.getheaders())
            print(f.read().decode())

        self.wfile.write(bytes(MESSAGE_RESPONSE, "utf-8"))

        print("-----------------------------------------------------")


server_address = ('', PORT)
httpd = http.server.HTTPServer(server_address, CustomHTTPRequestHandler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()

