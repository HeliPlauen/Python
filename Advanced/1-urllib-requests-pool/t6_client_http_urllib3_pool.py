
import time
import json
import urllib3


pool = urllib3.PoolManager(num_pools=2)

response1 = pool.request('GET', "http://127.0.0.1:8888")
print(response1)
#print(response1.read())
time.sleep(1)

dict_data = {"key": "value", "key2": "value2"}
str_data = json=json.dumps(dict_data)
data = bytes(str_data, "utf-8")
#response2 = pool.request('PUT', "http://127.0.0.1:8080", fields=dict_data)
#response2 = pool.request('PUT', "http://127.0.0.1:8080", body=str_data
response2 = pool.request('GET', "http://127.0.0.1:8080")
print(response2)
#print(response2.read())
time.sleep(1)

response3 = pool.request('GET', "http://127.0.0.1:9999")
print(response3)
#print(response3.read())
time.sleep(1)

print(len(pool.pools))
time.sleep(10)







