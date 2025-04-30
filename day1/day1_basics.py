# Use IDLE's interactive shell to see the 
# result of each line

# First Python Program
print("Hello, Workshop2025")

# Print a number
print(1)

# Perform mathematicl operations
print(3+2)
print(3-2)
print(3/2)
print(3*2)
print(3//2) # Integer division
print(3**2) # 3 to the power of 2
print(3**(1/2)) # Square root of 3
print(3%2) # modulo (remainder) returns 1

# Data types
number = 13 # Integer
number2= 3.14 # Float
Word="Hello" # String
Flag=True # Boolean
Numbers=[13,4,5,1] # List
Numbers2={14,8,99} # Set
Numbers3=(144, 98) # Tuple
Data={"Name":"Maamoun", "Age":44} # Dictionary

# How to check the data type?
print(type(Flag)) # returns <class 'bool'>

# Basic string operations
text="Good Morning"
print(text) # prints Good Morning
print(text[0]) # Prints G 
print(text.split(" ")) # Prints ['Good','Morning']
print(text.split(" ")[0]) # Prints Good
multiline="Good\nBad\nUgly" # Multiline text
print(multiline.split("\n")) # Prints: ['Good','Bad','Ugly]
print(multiline.split("\n")[1]) # Prints: Bad
Time="12: 03:44 " # Notic the spaces
print(Time.split(":").strip()) # Prints: ['12','03','44']
print(Time.split(":")[1].strip()) # Prints:03

# String concatenation
firstName="Maamoun"
lastName="Ahmed"
fullName=firstName+" "+lastName
print(fullName) # Prints Maamoun Ahmed
print(len(fullName)) # Prints the length of the name

# Print formatting
name="Maamoun"
print(f"Your name is {name}") # Prints: Your name is Maamoun

# User Input
name=input("Please enter your name: ") # String by default
number=int(input("Enter a number: ")) # To accept an integer
distance=float(input("Distance to x location? ")) # To accept a float
