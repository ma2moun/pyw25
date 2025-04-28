import json

# a Python object (dict):
x = {
  "name": "Mohammed",
  "age": 20,
  "job": "Engineer"
}

# convert to JSON using dumps:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# Save to a file
json_file=open("out.json", "w")
json_file.write(y)
