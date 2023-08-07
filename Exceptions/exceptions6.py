
# Exceptions ierarchy (right order!)

class FileException(Exception): ...
class FileNotFound(FileException): ...
class FileNotAlailable(FileNotFound): ...


print("-----------------------------------------------------------------------")

# Right
for error in [FileException, FileNotFound, FileNotAlailable]:
    try:
        raise error()
    except FileNotAlailable:
        print("FileNotAlailable")   # The highest preority
    except FileNotFound:
        print("FileNotFound")
    except FileException:
        print("FileException")      # The least preority


print("-----------------------------------------------------------------------")

# Wrong
for error in [FileException, FileNotFound, FileNotAlailable]:
    try:
        raise error()
    except FileNotFound:
        print("FileNotFound")        # Calls for 2 times!!! 
    except FileNotAlailable:
        print("FileNotAlailable")     
    except FileException:
        print("FileException")


print("-----------------------------------------------------------------------")

# Wrong2
for error in [FileException, FileNotFound, FileNotAlailable]:
    try:
        raise error()
    except FileException:
        print("FileException")       # Calls for 2 times!!!
    except FileNotAlailable:
        print("FileNotAlailable")
    except FileNotFound:
        print("FileNotFound")
    