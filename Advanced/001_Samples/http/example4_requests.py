import requests

# pip install requests
# запускаем различные виды запросов, но уже с использованием
# библиотеки requests
response1 = requests.get('http://example.com/')
print(response1)
response2 = requests.put('http://example.com/')
print(response2)
response3 = requests.post('http://example.com/')
print(response3)
response4 = requests.delete('http://example.com/')
print(response4)


"""
response1 = requests.get('https://devpython.ru')
response2 = requests.put('https://devpython.ru')
response3 = requests.post('https://devpython.ru')
response4 = requests.delete('https://devpython.ru')
"""
