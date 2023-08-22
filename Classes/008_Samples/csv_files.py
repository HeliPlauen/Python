import csv

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [row for row in csv_reader]

data.append(['Mike', '35', 'male'])
print(data)

# To avoid '\n' symbols use   " newline='' "   !!!!!
with open('data2.csv', 'w', newline='') as data_file:
    csv_writer = csv.writer(
        data_file,
        delimiter=','
    )
    for row in data:
        print(row)
        csv_writer.writerow(row)
