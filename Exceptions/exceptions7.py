
# Ladder of exceptions (Stacktrace manipulation) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def complicated_implementation():
    try:
        a = 1 / 0
    except ZeroDivisionError as err:
        try:
            raise RuntimeError("First call") from err    # Call the RuntimeError. We connect RuntimeError to ZeroDivisionError!!!
        except RuntimeError as err2:                     # Process THIS RuntimeError!!!! 
            try:
                a = [1, 2, 3]
                print(a[255])
            except IndexError as index_err:
                raise RuntimeError("Second challenge") from index_err   # We connect IndexError to RuntimeError!!!
                # We receive all 3 exceptions in the end!!!!! (fll three lincked to each other)
            

def easy_implementation():
    try:
        a = 1 / 0
    except ZeroDivisionError as err:
        raise RuntimeError("First call") from err


def main():
    #complicated_implementation()
    easy_implementation()


if __name__ == "__main__":
    main()