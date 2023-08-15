
# Recursion
def get_value(some_list, counter = 0):  
    if len(some_list) == 0:
        return
    if counter < len(some_list):
        some_element = some_list[counter]        
    if not isinstance(some_element, list):
        print(some_element)
        counter += 1
        get_value(some_list, counter)
    else:
        new_list = some_element
        print(new_list)
        counter = 0
        get_value(new_list, counter)


some_simple_list = [1, 2, [3, 4, [5, [6, []]]]]
get_value(some_simple_list)



