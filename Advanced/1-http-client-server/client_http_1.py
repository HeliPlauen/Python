
import time
import json
import urllib.request
import sys
import urllib.parse


ADDRESS = "http://127.0.0.1:8888"

ADDRESS_FOR_REQUEST = "http://127.0.0.1"
PORT_FOR_REQUEST = 8080
METHOD_FOR_REQUEST = "POST"


dict_data = {
    "url": ADDRESS_FOR_REQUEST,
    "port": PORT_FOR_REQUEST,
    "method": METHOD_FOR_REQUEST
}
str_data = json.dumps(dict_data)
data = bytes(str_data, "utf-8")

request4 = urllib.request.Request(url=ADDRESS, data=data, method="POST")
request4.add_header("Host", ADDRESS)
request4.add_header("Connection", "keep-alive")
request4.add_header("Accept", "text/plain")
print(request4.get_method())

with urllib.request.urlopen(request4) as response4: 
    print(response4.status)
    print(response4.reason)
    print(response4.getheaders())
    print(response4.getheader('Server'))
    print(response4.read().decode("utf-8"))

time.sleep(30)








