
import time
import threading


def task(event) -> None:
    i = 0
    while True:
        i += 1
        print(f'Running #{i}')
        time.sleep(1)
        if event.is_set():
            print('The thread was stopped prematurely.')
            break
        else:
            print('The thread was NOT stopped.')


def main() -> None:

    event = threading.Event()
    thread = threading.Thread(target=task, args=(event,))
    
    # start the thread
    thread.start()

    # suspend  the thread after 3 seconds
    time.sleep(3)

    # stop the child thread
    event.set()    
   

if __name__ == '__main__':
    main()
