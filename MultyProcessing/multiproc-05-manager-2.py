
import multiprocessing


def f(m_dict, m_array):
    m_dict["name"] = "test"
    m_dict["version"] = "1.0"
    m_array.append(1)
    m_array.append(2)


if __name__ == "__main__":
    with multiprocessing.Manager() as m:
        d = m.dict()
        l = m.list()
        pr = multiprocessing.Process(target=f, args=(d, l))
        pr.start()
        pr.join()

        print(f"dict: {d}")
        print(f"list: {l}")
