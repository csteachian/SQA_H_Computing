# 1001Task2.py
# Standard Algorithms - Finding Min + Max

# Predict and run

from random import *

numbers = []

def random20numbers():
  for x in range(20):
    numbers.append(randrange(1,3))
  return numbers

def displayNumbers (numbers):
  for x in range(20):
    print  (numbers[x]," ",end="")
  return

def findingMin (numbers):
  max = numbers[0]
  for x in range(1,20):
    if numbers[x] > max:
      max = numbers[x]
  print()
  print("The highest number (maximum) in the list is",max,".")
  return

numbers = random20numbers()
displayNumbers(numbers)
findingMin(numbers)
