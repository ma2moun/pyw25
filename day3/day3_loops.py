# Basic for loop:
for i in 1,2,3:
    print(f"The value of i={i}")

# Loop over a list:
numbers=[12,3,5,99,-11]
for number in numbers:
    print(f"The current number is: {number}")

# Using the range function
for i in range(5):
    print(f"Current number is: {i}") #output 0 to 4

# Using the range function with specifying the start
for i in range(1,5):
    print(f"Current number is: {i}") #prints 1 to 4

# Using the range function with specifying the start and step
for i in range(1,11,2):
    print(f"Current number is: {i}") #prints 1,3,5,...

# Countdown loop:
for i in range(10,0,-1):
    print(f"Current number is: {i}") 
print("Gooo!") # countdown to 1, then prints gooo!

# Demonstrating while loops
print("While Loop Example")
count = 1 # The start
while count <= 5: # Condition
    print(f"Count is: {count}")
    count += 1 # Step
print("While loop finished")

# While loop over uncounted number
choice=input("Do you want to continue? (y/n):").lower()
while choice!="n":
    print("Good")
    choice=input("Do you want to continue? (y/n):").lower()
print("You choose to exit, bye!")

# Demonstrating for loops with range
print("\nFor Loop Example")
for i in range(1, 6):  # 1 to 5
    print(f"Number: {i}")
print("For loop finished")

# Iterating through a string
print("\nString Iteration Example")
word = "Python"
for char in word:
    print(char)

# Using break
print("\nBreak Example")
for i in range(1, 10):
    if i == 6:
        print("Breaking the loop at 6")
        break
    print(i)

# Using continue
print("\nContinue Example")
for i in range(1, 8):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(f"Odd number: {i}")


# Nested for loops:
for i in range(1,6):
    for j in range(1,6):
        print(f"i={i} and j={j}") # 25 iterations (5*5)

# Nested while loops:
i=1
j=1
while i<=5:
    while j<=5:
        print(f"i={i} and j={j}")
        j+=1
    i+=1

