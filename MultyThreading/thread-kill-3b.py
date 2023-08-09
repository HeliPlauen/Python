

# Python program killing
# threads using stop
# flag
 
import threading
import time
 

def run(stop):
    while True:
        print('thread running')
        if stop():
            print("Stop!")
            break
        time.sleep(1)
 
            
def main():
    stop_threads = False
    t1 = threading.Thread(target = run, args =(lambda : stop_threads,))
    t1.start()
    time.sleep(10)
    stop_threads = True
    t1.join()
    print('thread killed')


if __name__ == "__main__":
    main()