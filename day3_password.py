limit=5
guess=0

password="myP@ssw0rd"

while guess<limit:
    Try=input("Guess a password: ")
    if Try!=password:
        guess+=1
        print(f"Try again, you still have {limit-guess} tries")
    else:
        print(f"Excellent! You guessed the password after {guess} tries")
print("Game over! No more tries")



