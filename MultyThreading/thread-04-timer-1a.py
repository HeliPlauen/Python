
import time
import threading


def test():
	while True:
		print("test")
		time.sleep(1)


thr = threading.Timer(5, test)
thr.start()


for _ in range(3):
	print("1111")
	time.sleep(1)


thr.cancel()  # Cancels Timer if it was not started
