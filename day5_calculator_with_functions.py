# Function to get two numbers from the user
def get_numbers():
    firstNumber = int(input("Enter the first number: ")) #only once
    secondNumber = int(input("Enter the second number: ")) #only once
    return firstNumber, secondNumber

# addition
def add(firstNumber, secondNumber):
    return firstNumber + secondNumber

# subtraction
def subtract(firstNumber, secondNumber):
    return firstNumber - secondNumber

# multiplication
def multiply(firstNumber, secondNumber):
    return firstNumber * secondNumber

# division
def divide(firstNumber, secondNumber):
    if secondNumber == 0:
        return "Zero division error"
    else:
        return firstNumber / secondNumber

# Main program loop
def calculator():
    while True:
        choice = int(input("Choose the operation:\n(1 to add)\n(2 to subtract)\n(3 to multiply)\n(4 to divide)\n(5 to exit): "))

        if choice == 1:
            firstNumber, secondNumber = get_numbers()
            print(f"The result of the addition is: {add(firstNumber, secondNumber)}")
        elif choice == 2:
            firstNumber, secondNumber = get_numbers()
            print(f"The result of the subtraction is: {subtract(firstNumber, secondNumber)}")
        elif choice == 3:
            firstNumber, secondNumber = get_numbers()
            print(f"The result of the multiplication is: {multiply(firstNumber, secondNumber)}")
        elif choice == 4:
            firstNumber, secondNumber = get_numbers()
            print(f"The result of the division is: {divide(firstNumber, secondNumber)}")
        elif choice == 5:
            print("Thank you for using my calculator.\nGood bye!")
            break
        else:
            print("Enter a valid choice!")

calculator()
