import random
import os
from datetime import datetime

# Load questions from a file
def load_questions(filename):
    questions = []
    try:
        with open(filename, 'r') as file:
            lines = file.read().split('\n\n')
            for block in lines:
                lines_in_block = block.strip().split('\n')
                if len(lines_in_block) >= 5:
                    question = lines_in_block[0][3:]  # Skip 'Q: '
                    options = [line for line in lines_in_block[1:5]]
                    answer = lines_in_block[5].split(':')[1].strip()
                    questions.append({
                        'question': question,
                        'options': options,
                        'answer': answer
                    })
    except FileNotFoundError:
        print("Questions file not found!")
    return questions

# Ask a single question
def ask_question(q):
    print("\n" + q['question'])
    for option in q['options']:
        print(option)
    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").upper()
        if user_answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print("Invalid input. Please choose A, B, C, or D.")
    return user_answer == q['answer']

# Save the score
def save_score(username, score, total):
    try:
        # change the line below based on your own directory structure
        with open('day8\\scores.txt', 'a') as file:
            now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            file.write(f"{username}: {score}/{total} at {now}\n")
    except Exception as e:
        print("Error saving the score:", e)

# Main program
def main():
    os.system('cls' if os.name == 'nt' else 'clear') #clear the screen
    print("Welcome to the Python Quiz App!")
    username = input("Enter your name: ")
    # change the line below based on your own directory structure
    questions = load_questions('day8\\questions.txt')

    if not questions:
        print("No questions to display. Exiting...")
        return

    random.shuffle(questions)  # Shuffle questions

    score = 0
    for q in questions:
        if ask_question(q):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    if score>12:
        print(f"\nExcellent job {username}! your final score is {score} out of {len(questions)}")
    elif score >9 and score <=12:
        print(f"\nVery good job {username}! your final score is {score} out of {len(questions)}")
    elif score>7 and score<=9:
        print(f"\nNot bad {username}, your final score is {score} out of {len(questions)}")
    elif score>5 and score<=7:
        print(f"\n{username},you need to work harder, your final score is {score} out of {len(questions)}")
    else:
        print(f"\nWhat are you doing, {username}? you need to work harder, your final score is {score} out of {len(questions)}")


    save_score(username, score, len(questions))

if __name__ == "__main__":
    main()
