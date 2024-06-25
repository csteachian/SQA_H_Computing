# 2. Create a program which creates a 1D array of 10 random numbers (from 1-100)
# and then uses a fixed loop to display them on the screen.

import random

numbers = []

for count in range(10):
    newNumber = random.randint(1,100)
    numbers.append(newNumber)

for count in range(10):
    print("Random number",str(count+1),":",numbers[count])