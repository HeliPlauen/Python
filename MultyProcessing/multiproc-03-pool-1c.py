import multiprocessing


def end_func(response):
    print("Task is over!")
    print(response)


def get_value(value):
    name = multiprocessing.current_process().name
    print(f"[{name}]value: {value}")
    return value


if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count()*3) as p:
        p.map_async(get_value, list(range(100)), callback=end_func)
        p.close()
        p.join()


