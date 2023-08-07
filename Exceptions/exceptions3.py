
# Silence the errors (ignore them)!!! Good and bad implementation

from contextlib import suppress


def bad_implementation(x, y):
    try:
        result = x / y
        print(f"Result: {result}")
    except:
        pass                             # Silence the error!!! (Bad way)


def good_implementation(x,  y):
    with suppress(ZeroDivisionError):    # Silence the error!!! (Good way) (Ignore mistakes if it is necessary!!!)
        result = x / y
        print(f"Result: {result}")


def read_file_implementation(filename):
    with suppress(FileNotFoundError, PermissionError):   # Silence the error!!! (Good way) (Ignore mistakes if it is necessary!!!)
        with open(filename) as file:
            content_chars = len(file.read())
            print(f"File characters: {content_chars}")


if __name__ == "__main__":
    bad_implementation(10, 0)
    good_implementation(10, 0)
    read_file_implementation("exceptions3.py")
    read_file_implementation("file.txt")
    print("Successfully finished!!!")
