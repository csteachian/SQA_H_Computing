from dataclasses import dataclass

@dataclass
class person():
  height : float = 0.0
  weight : float = 0.0
  bmi : float = 0.0

def displayData(myPeopleArray):
  for index in range(0,20):
    print(index,myPeopleArray[index].height, myPeopleArray[index].weight, myPeopleArray[index].bmi)

people = [person() for index in range(0,20)]

#print(people)

for index in range(0,20):
  people[index].height = float(input("Enter your height: "))
  people[index].weight = float(input("Enter your weight: "))

displayData(people)