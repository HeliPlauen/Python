
import time
import json
import random
import urllib.request
import sys
import urllib.parse


ADDRESS = "http://127.0.0.1:8888"


print("GET3:")
request2 = urllib.request.Request(url=ADDRESS, method="GET")
request2.add_header("Host", ADDRESS)
request2.add_header("Connection", "keep-alive")
request2.add_header("Accept", "text/html")
print(request2.get_method())

with urllib.request.urlopen(request2) as response2:
    print(response2.getcode())
    print(response2.msg)
    print(response2.getheaders())
    print(response2.getheader('Server'))
    data = response2.read()
    print(data.decode("utf-8"))
print("\n")


time.sleep(1)


print("POST2:")
ID = random.randint(1, 99999)
dict_data = {
    "key":f"REQUEST JSON {str(ID)}"
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
print("\n")


time.sleep(1)


print("NO-POST3:")
ID = random.randint(1, 99999)
data = urllib.parse.urlencode({"key": ID, "key2": ID})
print(f"{data} - type:{type(data)}")
data = data.encode("utf-8")
print(f"{data} - type:{type(data)}")


"""
with urllib.request.urlopen(url=ADDRESS, data=data) as response4: 
    print(response4.status)
    print(response4.reason)
    print(response4.getheaders())
    print(response4.getheader('Server'))
    print(response4.read().decode("utf-8"))
print("\n")
"""


time.sleep(10)








