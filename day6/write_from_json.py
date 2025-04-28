import json

# JSON data
x =  '{ "name":"Ahmed", "age":30, "city":"Muscat"}'

# parse x using loads:
y = json.loads(x)


# If reading from a json file:
with open("day6\\readthis.json") as f:
    y2=json.load(f)


# the result is a Python dictionary:
print(y["age"])
# print the dictionary
print(f"Data from the x JSON: {y}")

# or the data from the file:
print(f"Data from the file: {y2}")

