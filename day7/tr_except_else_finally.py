# this script will try to read from a file that doesn't exist
# the except will raise an error and it will create the file

try:
    filename = "day7\\myfile.txt"
    with open(filename,"r") as f:
        content=f.read()
except FileNotFoundError:
    print(f"Error: The File {filename} Not Found!")
    with open(filename,"x") as f:
        pass
    print(f"File {filename} was created successfully")
else:
    print(f"The file content are {content}")
finally:
    print("File operation attempt completed.")
    print("Bye")

