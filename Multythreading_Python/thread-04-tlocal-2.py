
import time
import threading


data = threading.local()


def get():
    print(data.value)


def t1():
    data.value = 1111
    get()
    print(f"t1: {data.value}")


def t2():
    data.value = 2222
    get()
    print(f"t2: {data.value}")


threading.Thread(target=t1).start()
threading.Thread(target=t2).start()


