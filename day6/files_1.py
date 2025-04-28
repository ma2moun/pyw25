file=open("myfile2.txt", "w")
file.write("This is the first line1\n")
file.write("This is the second line1\n")
file.write("This is the third line1\n")
#file.close() #uncomment this after creating the read
#alternatively, either close file, or change file2 to file
#then close it after reading
print("Done writing the file!")

file2=open("myfile2.txt", "r")
content=file2.read()
print(content)

