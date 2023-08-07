
# Good and bad implementations

import sys
import traceback


class Logger:
    def write_to_log(text):
        print("=" * 48)
        print(text)
        print("=" * 48)


def bad_implementation():
    print("Bad implementation")

    try:
        age = int(input("Input your age: "))
        work_experiance = int(input("Input your work experiance: "))
        print(f"result: {age / work_experiance}")
    except:
        print("\nThe program finished successfully!\n")


def good_implementation():
    print("Good implementation")

    try:
        age = int(input("Input your age: "))
        work_experiance = int(input("Input your work experiance: "))
        print(f"result: {age / work_experiance}")
    except ZeroDivisionError:
        print(f"\nZero division error!!! [{age} / {work_experiance}]\n")
    except ValueError:
        print("\nIntegers data type are expected!!! Not strings!!!\n")
    except KeyboardInterrupt:
        print("\nThe program finished successfully!\n")


def my_implementation():
    print("My implementation")

    try:
        age = int(input("Input your age: "))
        work_experiance = int(input("Input your work experiance: "))
        print(f"result: {age / work_experiance}")
    except Exception as err:
        print(f"\nProgram occures error!!! Exception: {err}\n")


if __name__ == "__main__":
    try:
        bad_implementation()
        good_implementation()
        my_implementation()
    except Exception:
        Logger.write_to_log(traceback.format_exc())

