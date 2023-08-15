import socket

# создание TCP-сокета
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# подключение к серверу используя доменное имя и порт
# можно также использовать IP-адрес
sock.connect(('example.com', 80))
# подготавливаем данные запроса, записываем в виде массива, чтоба разделять
# логические куски- далее будем склеивать строки.
content_items = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    # две пустые строки- завершение тела запроса (на склеивании будет два \n
    '\n'
]
# собираем запрос, используя перенос строки в качестве разделителя (\n)
content = '\n'.join(content_items)

print('--- HTTP MESSAGE ---')
print(content)
print('--- END OF MESSAGE ---')
# отправляем текстовый запрос на открытый сокет example.com:80
sock.send(content.encode())
# читаем данные с сокета в размере 10024- тут можно указывать конкретное
# значение, которое описано в спецификации протокола. В данном случае 10024
# указано просто в качестве примера- лучше использовать степень 2
# (например: 1, 2, 4, 8, 16, 32, 64, 128, 512, 1024, 2048, ...)
result = sock.recv(10024)
# печатаем данные полученные с сокета, декодируя байты в строку
print(result.decode())
