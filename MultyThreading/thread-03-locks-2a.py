import time
import threading


value = 0
locker = threading.Lock()      # Create lock


def inc_value():
	global value
	while True:
		with locker:           # Gets access to data and denies access for other threads, then Lets access to data for other threads
			value += 1
			time.sleep(1)
			print(value)


for _ in range(5):
	threading.Thread(target=inc_value).start()

