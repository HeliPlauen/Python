
import time
import json
import random
import urllib.request
import sys


ADDRESS = "http://127.0.0.1:8888"


print("GET1:")
response = urllib.request.urlopen(url=ADDRESS)
print(response.getcode())
print(response.msg)
print(response.getheaders())
print(response.getheader('Server'))
data = response.read()
print(data.decode("utf-8"))
print("\n")


time.sleep(1)


print("GET2:")
request2 = urllib.request.Request(url=ADDRESS, method="GET")
request2.add_header("Host", ADDRESS)
request2.add_header("Connection", "keep-alive")
request2.add_header("Accept", "text/html")
print(request2.get_method())

response2 = urllib.request.urlopen(request2)
print(response2.getcode())
print(response2.msg)
print(response2.getheaders())
print(response2.getheader('Server'))
data = response2.read()
print(data.decode("utf-8"))
print("\n")


time.sleep(1)


print("POST1:")
ID = random.randint(1, 99999)
dict_data = {
    "key":f"REQUEST JSON {str(ID)}"
}
str_data = json.dumps(dict_data)
data = bytes(str_data, "utf-8")
request3 = urllib.request.Request(url=ADDRESS, data=data, method="POST")
request3.add_header("Host", ADDRESS)
request3.add_header("Connection", "keep-alive")
request3.add_header("Accept", "text/plain")
print(request3.get_method())

response3 = urllib.request.urlopen(request3)
print(response3.getcode())
print(response3.msg)
print(response3.getheaders())
print(response3.getheader('Server'))
data = response3.read()
print(data.decode("utf-8"))

print("\n")


time.sleep(10)








