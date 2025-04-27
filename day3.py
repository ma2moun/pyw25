count=0
limit=5
yes_answers=["yes", "Yes", "Y"]
print(f"You have {limit} tries...")
choice=input("Do you want to continue (y/n) ")
while(choice in yes_answers):
    print("Money")
    count+=1
    print(f"Now you have {limit-count} tries left")
    if count==limit:
        print(f"You have reached {limit} tries")
        break
    choice=input("Do you want to continue (y/n) ")
