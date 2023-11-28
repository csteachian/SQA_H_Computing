def getTarget():
  targetAnimal = input("Please enter the target animal you are searching for")

  return targetAnimal

def getCircusAnimalsList():
  animals = ["giraffe", "chicken", "lion", "cheetah", "rat", "elephant", "snake", "chicken", "horse"]

  return animals

def countOccurrences(targetAnimal, animals):
  occurrences = 0
  for i in range(len.......):
    if animals[i] == ......:

def printOccurrences(occurrences):
  print(occurrences)


#*************  MAIN *************

targetAnimal = getTarget()
animals= getCircusAnimalsList()
occurrences = countOccurrences(targetAnimal, animals)
printOccurrences(occurrences)