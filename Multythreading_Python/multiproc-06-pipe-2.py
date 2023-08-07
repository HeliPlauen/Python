
import time
import multiprocessing


def send_data(conn):
    conn.close()
    conn.send("Hello world!")   # It closes channel only for itself
    

def send_data2(conn):
    conn.send("Hello 2!")


if __name__ == "__main__":
    output_c, input_c = multiprocessing.Pipe()
    multiprocessing.Process(target=send_data, args=(input_c,)).start()
    multiprocessing.Process(target=send_data2, args=(input_c,)).start()
    print("data: ", output_c.recv())

