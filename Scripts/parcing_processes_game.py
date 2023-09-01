
import psutil
import json


# python parcing_processes_game.py

filename = "file_game.json"

def check_if_game_process_exists():
    process_list = psutil.process_iter(['pid', 'name'])
    all_processes_list = [process.info for process in process_list]
    return all_processes_list

data = check_if_game_process_exists()

with open(filename, "w") as f:
    json.dump(data, f)