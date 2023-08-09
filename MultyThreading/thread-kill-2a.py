
import time
import threading


class Worker(threading.Thread):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event

    def run(self) -> None:
        i = 0
        while True:
            i += 1
            print(f'Running #{i}')
            time.sleep(1)
            if self.event.is_set():
                print('The thread was stopped prematurely.')
                break
            else:
                print('The thread was NOT stopped.')


def main() -> None:

    # create a new Event object
    event = threading.Event()

    # create a new Worker thread
    thread = Worker(event)
    
    # start the thread
    thread.start()

    # suspend  the thread after 3 seconds
    time.sleep(3)

    # stop the child thread
    event.set()    
   

if __name__ == '__main__':
    main()
