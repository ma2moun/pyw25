import csv

with open("day6\\data.csv", "r") as f:
    csvreader=csv.reader(f)
    for line in csvreader:
        print(line)


