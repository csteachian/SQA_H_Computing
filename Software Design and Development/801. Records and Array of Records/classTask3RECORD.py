# 206 Parallel Arrays - Task 3 (BUT AS RECORDS)
# By Mr Simpson

# Write a program that will ask the user for their name and
# a test mark out of 100.
 
# This should be looped five times and the names and marks
# should be stored in separate arrays. 

# Print out the contents of the names and the marks arrays. 

from dataclasses import dataclass
@dataclass
class PERSON():
    name : str = ''
    mark : int = 0

# subroutines
def get_name():
    thisName = input("Enter your name:")
    return thisName

def get_test_mark():
    thisMark = int(input("Enter test mark (0-100):"))
    while thisMark < 0 or thisMark > 100:
        print("Error!!!!!!! Fool!!!!!")
        thisMark = int(input("Enter test mark (0-100):"))
    return thisMark

def display_all(people):
    for index in range(5):
        print(people[index].name + " scored " + str(people[index].mark))

# top level design
people = [PERSON(), PERSON(), PERSON(), PERSON(), PERSON()]
for index in range(5):
    people[index].name = get_name()
    people[index].mark = get_test_mark()
display_all(people)