person={
    "Name":"Ahmed",
    "Age": 22,
    "Job": "Engineer",
    "is_student":False
}
#methods
print("\nDictionary methods:")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Modifying dictionaries
print("\nModifying dictionaries:")
person["Age"] = 29
print(f"Updated age: {person['Age']}")

# Removing items
removed_value = person.pop("is_student")
print(f"Removed is_student ({removed_value}): {person}")

print(person)
print(person["Age"])
person["Age"]=23
print(person)

person["Nationality"]="Omani" #new item
print(person)

"""
Below is a dictionary where the values are dictionaries
"""
students={
    "Ahmed":{
        "SID":111222,
        "Age":21,
        "GPA":3.2},
    "Sami":{
        "SID":112211,
        "Age":22,
        "GPA":2.7}}

print(students["Ahmed"]["Age"]) #prints 21

for key,value in students.items():
    print(f"{key}:")
    for k, v in value.items():
        print(f"- {k} :{v}")


name = input("Enter name: ")

if name in students: #check before adding
    print(f"Contact '{name}' already exists!")
sid=int(input("Enter the student ID: "))
age=int(input("Enter the student age: "))
GPA=float(input("Enter the student GPA: "))
students[name]={
    "SID":sid,
    "Age":age,
    "GPA":GPA
}

print(f"Details of student {name} has been added successfully!")


