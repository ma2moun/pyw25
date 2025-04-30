time="12: 33:01 " #notice the spaces

# To create a list of the hours, minutes, and seconds
Time=time.split(":")
print(Time)

# To print a single item
print(time.split(":")[1])

# To print a single item without the whitespace
print(time.split(":")[1].strip())

question="""
Q: Which of these is NOT a valid file mode when opening a file?
A) 'r'
B) 'w'
C) 'e'
D) 'a'
ANSWER: C
"""

# To save each line as an item in a list
lines=question.split("\n")
print(f"list of lines:\n {lines}")

# To print the question alone
question1=question.split("\n")[1]
print(f"The question alone: {question1}")

# To print the question alone and remove leading/tailing spaces
question2=question.split('\n')[1].strip()
print(f"The question alone (no spaces): {question2}")

# To remove the Q:

question3=question.split('\n')[1].strip()[3:]
print(f"The question alone (no Q: ): {question3}")

# to show the options:
options= [line for line in lines[2:6]]
print(f"Options are: {options}")

# The answer:
answer=question.split('\n')[-2].strip()[-1:]
print(f"the answer is: {answer}")
