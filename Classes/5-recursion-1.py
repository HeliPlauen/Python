
# Recursion
def return_val(number, counter=1, number_list = []):
    if number <= 0:
        return number_list 

    number_list.append(counter)
    return_val(number - 1, counter + 1, number_list)

    # Return final list
    return number_list  


print(return_val(10))






