# 1001Task6.py
# Standard Algorithms - Finding Min + Max

# Investigate and modify

from random import *

numbers = []

def random20numbers():
  for x in range(20):
    numbers.append(randrange(1,51))
  return numbers

def displayNumbers (numbers):
  for x in range(20):
    print  (numbers[x]," ",end="")

def findingMax(numbers):
  # WRITE CODE TO IMPLEMENT A FINDING MAX
  # ...
  print()
  print("The highest number (maximum) in the list is",max,".")

numbers = random20numbers()
displayNumbers(numbers)
findingMax(numbers)
