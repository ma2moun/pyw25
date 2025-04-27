try:
     age=int(input("How old are you?"))
except ValueError:
    print("YOu have to enter a number ")
    exit(0)
if(age<=0 or age>100):
    print("invalid Age")
    exit(0)
    
student=input("Are you a student? (yes or no)").lower()=="yes"
army=input("Are you an army soldier? (yes or no)").lower()=="yes"
member=input("Do you have a membership? (yes or no)").lower()=="yes"
discount=0
valid=False

if(age>=65 and age<100) :
    discount=10 #x
    valid=True
elif(student):
    discount=7#x
    valid=True
elif(army):
    discount=4#x
    valid=True
else:
    print("Sorry, no main discount")

if member:
    discount+=2.5
    valid=True
else:
    discount+=0

if(valid):
    print(f"You have a discount of {discount}")
else:
    print("You deserve nothing")