
import time
import threading


event = threading.Event()


def test():
    print("Test function started")
    while True:
        event.wait()                     # It does not work because event is False 
        print("test")
        time.sleep(1)


def test_event():
    while True:
        time.sleep(5)
        event.set()                      # Set True
        print("Event True")
        time.sleep(5)
        event.clear()                    # Set False
        print("Event False")


event.clear()                            # Event = False
threading.Thread(target=test).start()
threading.Thread(target=test_event).start()


