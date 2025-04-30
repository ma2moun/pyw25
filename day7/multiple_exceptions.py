print("\nMultiple exceptions:")
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the first number: ")
    result = int(num1) / int(num2)
    print(f"{num1} / {num2} = {result}")
except ZeroDivisionError: #num2=0
    print("Error: Cannot divide by zero!")
except ValueError: #enter a letter
    print("Error: Please enter a valid number!")
except Exception as e: #remove int() from any num to demonstrate
    print(f"An unexpected error occurred: {e}")
