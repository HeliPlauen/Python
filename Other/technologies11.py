
# Delete duplicates

from collections import OrderedDict

values = [1, 1, 2, 3, 4, 3]
print(OrderedDict.fromkeys(values).keys())
print(list(OrderedDict.fromkeys(values).keys()))


# and/or ??????

server1 = None
server2 = "server_2"
server3 = None
server4 = "server_4"

result = server1 or server2 or server3 or "servers_are_busy"
result2 = server1 and server2 and server3 and "servers_are_busy"

print(result)
print(result2)
