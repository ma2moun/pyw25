import csv

# The header of the columns
header=["ID", "Name", "Skill", "Experience"]

# The data
data=[
    [12,33,41,2],
    ["Majid", "Adam", "Manar", "Basem"],
    ["C++", "Research", "Driving", "Cooking"],
    [3, 5, 1, 12]
]

with open("day6\\skills.csv", "w") as f:
    csvwrite=csv.writer(f)
    csvwrite.writerow(header) # Write the header first
    csvwrite.writerows(data) # Write the whole data
print("Done writing the csv file!")
