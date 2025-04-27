"This is a simple if "

""" try:
    age=int(input("Enter your age: "))
    #exit if age is invalid
    if age<=0 or age>100:
        print("Invalid age!")
        exit(0)
except ValueError:
    print("Invalid age! Please enter a number.")
    exit(0) """











age=int(input("Enter your age: "))
is_student=input("Are you a student? (yes, no) ")
is_army=input("Do you server in the army? (yes, no) ")
is_member=input("Do you have a membership? (yes/no) ")

discount=0
valid=False

if (age>=65 and age<100):
    discount=10
    valid=True
    reason="Age"
elif (is_student=="yes"):
    valid=True
    discount=7
    reason="student"
elif (is_army=="yes"):
    valid=True
    discount=5
    reason="army"

else:
    print("Sorry, no discount available")


if(valid):
    print(f"Congrats! You desever a discount of {discount} because of {reason}")
    if (is_member=="yes"):
        valid=True
        add=2.5
        print(f"and you also deserve a discount of {add} because of your membership")
        print(f"Total discount is {discount+add}")
