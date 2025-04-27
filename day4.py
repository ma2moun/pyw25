import random

numbers=[]

for i in range(10):
    mark=random.randint(35,100)
    numbers.append(mark)

print(f"The list is {numbers}")

Max=max(numbers)
Min=min(numbers)
Sum=0
for i in numbers:
    Sum+=i

Avg=Sum/len(numbers)

print(f"The max is {Max}, min is {Min},"
       f"sum is {Sum}, and average is {Avg}")
