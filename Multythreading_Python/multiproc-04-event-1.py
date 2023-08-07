
import time
import multiprocessing


event = multiprocessing.Event()


def test(event):
    print("Test function started")  
    while True:
        event.wait()          # It does not work because event=False
        print("test")
        time.sleep(1)


def test_event(event):
    while True:
        time.sleep(5)
        event.set()           # Set True
        print("Event True")
        time.sleep(5)
        event.clear()         # Set False
        print("Event False")


if __name__ == "__main__":
    multiprocessing.Process(target=test, args=(event,)).start()
    multiprocessing.Process(target=test_event, args=(event,)).start()


