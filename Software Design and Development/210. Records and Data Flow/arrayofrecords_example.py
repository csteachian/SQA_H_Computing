from dataclasses import dataclass
@dataclass
class user():
    height : float = 1.87 # These are default values
    weight : float = 75.0
    BMI : float = 0.0

users = [user for i in range(10)] # Creates an array of identical users (for this example)

# Passing an array of records to a function - neat and tidy!
def calculateBMI(users):
    for i in range(len(users)):
        users[i].BMI = users[i].weight / (users[i].height ** 2)
    return users
  
# Can't get the order wrong - there's only one parameter!
calculateBMI(users)  # Easy!

