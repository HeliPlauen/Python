
import time
import multiprocessing


def getter(pipe):      # It will only get, not send
    out, inp = pipe
    inp.close()
    while True:
        try:
            print("data: ", out.recv())
        except:
            break


def setter(sequence, input_c):
    for item in sequence:
        time.sleep(1)
        input_c.send(item)


if __name__ == "__main__":
    output_c, input_c = multiprocessing.Pipe()
    g = multiprocessing.Process(target=getter, args=((output_c, input_c),))
    g.start()
    
    setter([1, 2, 3, 4, 5], input_c)
    output_c.close()
    input_c.close()


