
import time
import threading


event = threading.Event()


def image_handler():
    thr_num = threading.current_thread().name
    print(f"Prepearing image fropm thread: [{thr_num}]")
    event.wait()
    print("The image was sent")


for i in range(10):
    threading.Thread(target=image_handler, name=str(i)).start()
    print(f"Thread {i} started!")
    time.sleep(1)


if threading.active_count() >= 10:
    event.set()                      # Set True to the Event
