import random

mynumber=random.randint(1,10)
count=1
limit=5
guess=int(input(f"Guess the number ({limit} guesses max): "))
if(guess==mynumber):
        print("Congrats, you have used {count} guesses")

while(guess!=mynumber):
    if(count==limit):
        print(f"Game over, you have reached {count} times")
        break
    if(guess<mynumber):
        print("Go higher...")
    elif(guess>mynumber):
        print("Go lower")
    
    count+=1
    guess=int(input(f"Guess the number ({limit-count} guesses max): "))
    


     
        