import json

# JSON data
x =  '{ "name":"Ahmed", "age":30, "city":"Muscat"}'

#or read from a file:
""" json_file=open("out.json", "r")
x=json_file.read() """

# parse x using loads:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

# print the dictionary
print(y)
