
import time
import threading


def test():
	while True:
		print("test")
		time.sleep(1)


thr = threading.Timer(5, test)
thr.setDaemon(True)             # Aborts when the main thread is finished
thr.start()


for _ in range(6):
	print("1111")
	time.sleep(1)



