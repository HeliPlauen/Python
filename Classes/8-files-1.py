
import csv
import json
from xml.etree import ElementTree


# python 8-files-1.py
csv_filename = "titanic.csv"
json_filename = "titanic.json"
xml_filename = "titanic.xml"

# It is useless!!!
with open(csv_filename, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #print(list(csv_reader))

# Read from CSV 
with open(csv_filename, "r") as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)
    count = 0
    list_data = [row for row in csv_dict_reader]
    #print(list_data)

# Write down data into JSON
with open(json_filename, "w") as json_file:
    json.dump(list_data, json_file)

# Read data from JSON
with open(json_filename, "r") as json_file:
    list_data = json.load(json_file)
    #print(list_data)
    #print(len(list_data))

# Get keys
list_keys = list(list_data[886].keys())
#print(list_keys)

# Create XML data
data = ElementTree.Element("data")
passengers = ElementTree.SubElement(data, "passengers")
pass_list = []
for i in range(len(list_data)):
    pass_list.append(ElementTree.SubElement(passengers, "passenger"))

for i in range(len(pass_list)):
    item = pass_list[i]
    for j in range(len(list_keys)):
        item.set(list_keys[j], dict(list_data[i])[list_keys[j]])
        #if i == 0:
            #print(list_keys[j])
            #print(dict(list_data[i])[list_keys[j]])

# Write down data into XML file
xml_file = ElementTree.tostring(data)
with open(xml_filename, "wb") as file:
    file.write(xml_file)

