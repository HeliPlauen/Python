
import time
import threading


def test():
	while True:
		print("test")
		time.sleep(1)


threading.Timer(10, test).start()


while True:
	print("1111")
	time.sleep(1)


