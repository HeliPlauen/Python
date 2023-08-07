
# Ignore errors (2-nd way)

def download_source_code():
    try:
        temp = [1, 2, 3]
        result = temp[255]
    except Exception:
        pass                  # Silence the error!!! (Ignore them)


def main():
    download_source_code()


if __name__ == "__main__":
    main()
