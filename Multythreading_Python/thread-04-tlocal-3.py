
import time
import threading


data = threading.local()


def get_name():
    print(data.name)    # Something wrong, I don't know what


def t1():
    data.name = threading.current_thread().name
    time.sleep(100)


threading.Thread(target=t1, name="t1").start()
time.sleep(2)
get_name()


