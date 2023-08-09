import time
import threading
import os


locker = threading.RLock()      # We can NOT UNlock it from everywhere (from any other thread)


def inc_value(): 
    locker.acquire()
    trd_name = threading.current_thread().name
    print(f"{trd_name} started!!! [{time.time()}]") 


def unloc_thread():  
    try:
        time.sleep(10)
        locker.release()
        print(f"Unlocked! ({time.time()})") 
    except Exception as err:
        print(f"Error: {err}")
        os._exit(1)


threading.Thread(target=inc_value, name="thr_1").start()
threading.Thread(target=inc_value, name="thr_2").start()
threading.Thread(target=unloc_thread).start()              # Not Successfull attempt to unlock!!!!


