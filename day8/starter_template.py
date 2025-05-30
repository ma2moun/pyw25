## You need to fill in the TODO in order to have a complete project

# Import required libraries
import random
from datetime import datetime

# Function to load questions from a file
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

# Function to ask a single question to the user
def ask_question(question_data):
    # TODO: Display the question and options
    # TODO: Get user answer and check if it is correct
    return False

# Function to save the score into a file
def save_score(username, score, total_questions):
    # TODO: Save the user's name, score, and timestamp into 'scores.txt'
    pass

# Main function to run the quiz
def main():
    print("Welcome to the Python Quiz App!")
    username = input("Enter your name: ")
    questions = load_questions('day8\\questions.txt')
    if not questions:
        print("No questions available. Please check the file!")
        return

    random.shuffle(questions)  # Shuffle the questions

    score = 0

    for question in questions:
        if ask_question(question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}\n")

    print(f"{username}, your final score is {score} out of {len(questions)}")
    save_score(username, score, len(questions))

if __name__ == "__main__":
    main()
