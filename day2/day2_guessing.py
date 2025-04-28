import random #We will discuss it later


secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 10. You have {max_attempts} attempts.")


while attempts < max_attempts:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts!")
        break

    # remaining attempts
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"You have {remaining} attempts left.")

# Not guessed? game over.
if guess != secret_number:
    print(f"\nGame over! The number was {secret_number}.")
