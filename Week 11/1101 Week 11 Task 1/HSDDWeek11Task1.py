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

people[0].height = 100.0
people[0].weight = 40.0
people[0].bmi = 0.0

people[1].height = 150.0
people[1].weight = 50.0
people[1].bmi = 0.0

displayData(people)