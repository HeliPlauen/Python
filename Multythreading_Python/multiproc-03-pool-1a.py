import multiprocessing


def get_value(value):
    name = multiprocessing.current_process().name
    print(f"[{name}]value: {value}")


if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count()*3) as p:
        p.map(get_value, list(range(100)))


