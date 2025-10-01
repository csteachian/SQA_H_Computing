# 206 Parallel Arrays - Task 3
# By Mr Simpson

# Write a program that will ask the user for their name and
# a test mark out of 100.
 
# This should be looped five times and the names and marks
# should be stored in separate arrays. 

# Print out the contents of the names and the marks arrays. 

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

def display_all(aName, aMark):
    for index in range(5):
        print(aName[index] + " scored " + str(aMark[index]))

# top level design
name = []
mark = []
for index in range(5):
    name.append(get_name())
    mark.append(get_test_mark())
display_all(name, mark)