# 4. Create a program which asks the user for their name and then
# generates six random lottery numbers (from 1-50), storing these
# numbers in a 1D array. Create a suitable output for this program
# which displays their lottery ticket.

import random

name = input("Please enter your name: ")

numbers = []
for count in range(6):
    numbers.append(random.randint(1,50))

print("YOU ARE IN THE DRAW!")
print("Ticket holder:",name)
for count in range(6):
    print(numbers[count])
print("GOOD LUCK!!")