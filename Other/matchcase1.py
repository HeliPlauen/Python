

#args = "1"
#args = ["start"]
#args = ["start", "-h", "-k"]
#args = ["start", "-h"]
args = ["start", "alex192"]

black_list = ["alex1923", "1222"]


match args:
    case ["start"]:
        print("Add arguments!")

    case ["start", nickname] if nickname not in black_list:
        print(f"{nickname} - OK")

    case ["start", ("-h" | "--help" | "help") as hlp]:
        print(f"Arguments from user: {hlp}")

    case ["start", *args]:               # If more then one list element
        print(f"Arguments: {args}")

    case _:
        print[f"Default: {args}"]