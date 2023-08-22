
import re
import math
import sys


task = "To make calculations input:\n 'sum(2, 2)' to have sum af 2 and 2,\n 'sub(2, 2)' to substract 2 and 2,\n 'mult(2, 2)' to multiply 2 and 2,\n 'div(2, 2)' to divide 2 and 2,\n 'exp(2, 2)' to make exp 2 into 2,\n 'log(2, 2)' to get log of 2 by 2.\n           SO, INPUT YOUR TASK:"

#keys_list = [elem.replace("\'", "").replace("_", "").replace("a", "").replace("b", "", 1) for elem in re.findall(r"\'.+\'", task)]
keys_list = [elem.replace("\'", "").replace(",", "").replace("(", "").replace(")", "").replace("2", "").replace(" ", "") for elem in re.findall(r"\'.+\'", task)]

task_dictionary = dict.fromkeys(keys_list)

task_dictionary["sum"] = lambda a, b: a + b
task_dictionary["sub"] = lambda a, b: a - b
task_dictionary["mult"] = lambda a, b: a * b
task_dictionary["div"] = lambda a, b: a / b
task_dictionary["exp"] = lambda a, b: a ** b
task_dictionary["log"] = math.log


def arythmetic_func(oper, a, b):
    result = task_dictionary[oper](int(a), int(b))
    return result


try:
    while True:
        # Get data from user
        calculation_task = input(task)

        # Process user input
        processed_input_task = calculation_task.replace(" ", "").replace(",", " ").replace("(", " ").replace(")", "").split(" ")

        # Check user input
        if len(processed_input_task) != 3 or processed_input_task[0] not in keys_list:
            print("Incorrect user input!!!")
        else:
            print("User input - OK!!!")

            # Make calculations
            calculation_result = arythmetic_func(processed_input_task[0], processed_input_task[1], processed_input_task[2])
            print(f"RESULT: {calculation_result}")

            break

except KeyboardInterrupt:
    sys.exit(1)


