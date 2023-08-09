import time
import threading


value = 0


def inc_value():
	global value
	while True:
		value += 1
		time.sleep(1)
		print(value)


for _ in range(5):
	threading.Thread(target=inc_value).start()

