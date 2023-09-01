
import json


# python parcing_two_files.py

filename1 = "file_game.json"
filename2 = "file_no_game.json"

with open(filename1, "r") as f:
    data_game = json.load(f)
    print(len(data_game))

with open(filename2, "r") as f:
    data_no_game = json.load(f)
    print(len(data_no_game))

# Check processes by name
print("CHECK BY NAME")
difference_list = []
for process_game in data_game:
    flag = False
    process_game_name = process_game["name"]

    for process_no_game in data_no_game:
        if process_no_game["name"] == process_game_name:
            flag = True
            break

    # If data_no_game has already finished - append process into difference_list
    if flag == False:
        difference_list.append(process_game)

print(len(difference_list))
print(difference_list)
print("-------------------------------------------------------------------------------------")

# Check processes by id
print("CHECK BY ID")
difference_list = []
for process_game in data_game:
    flag = False
    process_game_ID = process_game["pid"]

    for process_no_game in data_no_game:
        if process_no_game["pid"] == process_game_ID:
            flag = True
            break

    # If data_no_game has already finished - append process into difference_list
    if flag == False:
        difference_list.append(process_game)

print(len(difference_list))
print(difference_list)

# os.system('taskkill /t /f /im "nvstreamer.exe"')   -   (+) YES!!!!
# os.system('taskkill /t /f /im "conhost.exe"')      -   Console!!!!
# os.system('taskkill /t /f /im "svchost.exe"')      -   (-)