
import os


print(os.name)
print(os.environ)

try:
    os.rename("test.txt", "pytest.txt")
except FileNotFoundError:
    print("File does not exist")


try:
    os.startfile(r'N:\YPROGRAMMING\Python\Scripts\labels.pdf')
except FileNotFoundError:
    print("File does not exist")