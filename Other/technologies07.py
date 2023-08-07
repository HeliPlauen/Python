
# Wrong and right way dealing with loops when you get number combunations

from itertools import product


list1 = [1, 2]
list2 = [3, 4]
list3 = [5, 6]


# Wrong
def lowqual_implementation():
    for a in list1:
        for b in list2:
            for c in list3:
                print(a, b, c)


# Right
def normal_implementation():
    for a, b, c in product(list1, list2, list3):
        print(a, b, c)


lowqual_implementation()
print("\n\n")
normal_implementation()