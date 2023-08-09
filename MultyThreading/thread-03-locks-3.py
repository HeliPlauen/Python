import time
import threading


locker = threading.Lock()      # We can UNlock it from everywhere  (from any other thread)


def inc_value(): 
    locker.acquire()
    trd_name = threading.current_thread().name
    print(f"{trd_name} started!!! [{time.time()}]")    


def unloc_thread():    
    time.sleep(10)
    locker.release()
    print(f"Unlocked! ({time.time()})")  


threading.Thread(target=inc_value, name="thr_1").start()
threading.Thread(target=inc_value, name="thr_2").start()
threading.Thread(target=unloc_thread).start()              # Unlock here!

