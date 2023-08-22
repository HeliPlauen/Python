
elem_str = "1_2,40_5,5_32"


new_list = [[int(number) for number in list_elem.split("_")] for list_elem in elem_str.split(",")]
print(new_list)

new_list_2 = [int(number) for list_elem in elem_str.split(",") for number in list_elem.split("_")]
print(new_list_2)

# The final result!!!
new_list_3 = [int(list_elem.split("_")[0]) + int(list_elem.split("_")[1]) for list_elem in elem_str.split(",")]
print(new_list_3)