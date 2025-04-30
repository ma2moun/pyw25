import math
import datetime
import time

timenow=time.time()
#timenow=timenow.strftime('%H:%M:%S')
""" 
for i in range(1000):
    print(i)
timethen=time.time()
result=timethen-timenow
print(f"Thhe time is {result:.2f}") """

## Using datetime Module
# Measure how long it takes to count
timenow=datetime.datetime.now()
timenow=timenow.strftime('%H:%M:%S')
h1=int(timenow[0:2])
m1=int(timenow[3:5])
s1=int(timenow[6:])
for i in range(10000):
    print(i)
timethen=datetime.datetime.now()
timethen=timethen.strftime('%H:%M:%S')
h2=int(timethen[0:2])
m2=int(timethen[3:5])
s2=int(timethen[6:])
print(f"It took from {h2-h1}:{m2-m1}:{s2-s1} to count to 100000")
#But, how to calculate the elapsed time exactly?


# Using math module
""" print("\nMath module:")
print(f"Square root of 16: {math.sqrt(16)}") #instead of 16**(1/2)
print(f"Pi: {math.pi}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"GCD of 24 and 36: {math.gcd(24, 36)}") """


