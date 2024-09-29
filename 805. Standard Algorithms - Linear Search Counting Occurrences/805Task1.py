# 805Task1.py
# Standard Algorithms - Linear Search & Counting Occurrences

# Predict and read

names = ['Jim', 'James', 'Jan', 'Jimmy', 'John', 'Jenna', 'Jonny' ]
counter = 0
nameToFind = 'John'
found = False
foundPosition = -1
while counter < len(names) and found == False:
  if names[counter] == nameToFind:
    found = True 
    foundPosition = counter
  else:
    counter = counter + 1

if found == True:
  print (nameToFind, " was found at position: ", foundPosition)
else:
  print (nameToFind, " wasn't found. Too bad.")