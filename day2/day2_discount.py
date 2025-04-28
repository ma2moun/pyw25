# Program to check eligibility for a discount
print("Discount Eligibility Checker")
print("--------------------------")

print("NOTE: Only the highest discount will be counted...")


age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"
is_army = input("Are you a veteran? (yes/no): ").lower() == "yes"
has_membership = input("Do you have a membership? (yes/no): ").lower() == "yes"


eligible = False
discount = 0

if age > 65:
    eligible = True
    discount = 10
    reason = "Over 65"
elif is_student:
    eligible = True
    discount = 7
    reason = "student"
elif is_army:
    eligible = True
    discount = 4
    reason = "army"

#check if user has a membership
if has_membership:
    discount += 2.5


if eligible:
    print(f"Congratulations! You are eligible for a {discount}% discount as a {reason}.")
    if has_membership:
        print(f"This includes your 2.5% membership bonus! Total of {discount+2.5}%")
else:
    if has_membership:
        print(f"You are eligible for a {discount}% discount with your membership.")
    else:
        print("Sorry, you are not eligible for a discount.")
