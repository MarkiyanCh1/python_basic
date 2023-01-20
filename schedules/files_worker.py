# Task 1 1) Create schedules/schedule.csv in any way available to you
# 1.1) Column names departure point; departure time; destination point; arrival time; cost ticket
# 1.2) Enter several lines of relevant data
import csv
import json


with open('schedule.csv', 'w') as csv_table:
    fieldnames = ['Departure point', 'Departure time', 'Destination point', 'Arrival time', 'Cost ticket']
    table_data = csv.DictWriter(csv_table, fieldnames=fieldnames)

    table_data.writeheader()
    table_data.writerow({'Departure point': 'Kyiv',
                         'Departure time': '12:30',
                         'Destination point': 'Lviv',
                         'Arrival time': '18:20',
                         'Cost ticket': '450 UAH'
                         })
    table_data.writerow({'Departure point': 'Kyiv',
                         'Departure time': '11:05',
                         'Destination point': 'Odesa',
                         'Arrival time': '17:10',
                         'Cost ticket': '470 UAH'
                         })

# Task 2 Create a function that reads the content of schedule.csv and returns the entire content of the file
# as a dictionary or list
list_empty = []
with open('schedule.csv', 'r') as schedule:
    reader = csv.DictReader(schedule)
    for row in reader:
        list_empty.append(row)
        print(row)


# Task 3 Create a function that writes the received content to the schedules/schedule.json file
# 3.1) The keys in the recorded file must be sorted.
# 3.2) Attachments within the file must be indented with 4 spaces.
with open('schedule.json', 'w', newline='') as fh:
    json.dump(list_empty, fh, indent=4, sort_keys=True)
