
# Bad implementation

def file_available(filename):
    return 0


def main():
    try:
        result = file_available("file.txt")
        if not result:
            raise Exception("File not available")
    except:
        raise


if __name__ == "__main__":
    main()
