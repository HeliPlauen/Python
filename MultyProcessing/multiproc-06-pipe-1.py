
import time
import multiprocessing


def send_data(conn):
    conn.send("Hello world!")
    conn.close()


if __name__ == "__main__":
    output_c, input_c = multiprocessing.Pipe()
    p = multiprocessing.Process(target=send_data, args=(input_c,))
    p.start()
    p.join()
    print("data: ", output_c.recv())

