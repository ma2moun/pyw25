print("\nReading line by line:")
file = open("sample.txt", "r") #this file should exist
lines = file.readlines() #read all lines
file.close()
for i, line in enumerate(lines, 1):
    print(f"Line {i}: {line.strip()}")
#See the difference
for line in lines:
    print(line)

print("Readline:")

File=open("sample.txt", "r")
print(File.readline().strip())
print(File.readline().strip())

#loop through the file:
with open("sample.txt") as f:
  for x in f:
    print(x.strip())


# to delete a file
#import os # put on top
#os.remove("sample.txt")

#Check first
"""
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist") """

# Remove a directory
"""
import os
os.rmdir("somefolder")
"""
