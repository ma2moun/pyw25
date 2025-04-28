# To demonstrate the calculator program without functions

choice=int(input("Choose the operation:\n(1 to add)\
    \n(2 to subtract) \n(3 to multiply) \
        \n(4 to divide) \n(5 to exit): "))

if choice==1:
    firstNumber=int(input("Enter the first number: "))
    secondNumber=int(input("Enter the second number: "))
    print(f"The result of the addition is: {firstNumber+secondNumber}")
elif choice==2:
    firstNumber=int(input("Enter the first number: "))#duplicate
    secondNumber=int(input("Enter the second number: "))#duplicate
    print(f"The result of the subtraction is: {firstNumber-secondNumber}")
elif choice==3:
    firstNumber=int(input("Enter the first number: "))#duplicate
    secondNumber=int(input("Enter the second number: "))#duplicate
    print(f"The result of the multiplication is: {firstNumber*secondNumber}")
elif choice==4:
    firstNumber=int(input("Enter the first number: "))#duplicate
    secondNumber=int(input("Enter the second number: "))#duplicate
    if secondNumber==0:
        print("Zero division error")
        exit(0)
    else:
        print(f"The result of the division is: {firstNumber/secondNumber}")
elif choice==5:
    print("Thank you for using my calculator.\nGood bye!")
    exit(0)
else:
    print("Enter a valid choice!")
