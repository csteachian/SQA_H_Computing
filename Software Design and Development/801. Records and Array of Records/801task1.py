from dataclasses import dataclass

@dataclass
class person():
  height : float = 0.0
  weight : float = 0.0
  bmi : float = 0.0

people = [person() for index in range(5)]

'''
Task 1

Using the program code above as a starting point, create the records for each of the five people listed below:

Person 0: height = 1.75, weight = 70.5
Person 1: height = 1.62, weight = 55.8
Person 2: height = 1.88, weight = 95.2
Person 3: height = 1.70, weight = 82.3
Person 4: height = 1.80, weight = 68.0

Remember to include the code to calculate the BMI of each person and display each record on the screen.
'''