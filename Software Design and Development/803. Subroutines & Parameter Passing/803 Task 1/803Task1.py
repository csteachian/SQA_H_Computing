#modular programming

def displayNames(nameList):
  print("Current list")
  for loop in range(len(nameList)):
    print("Forename",nameList[loop][0])
    print("Surname",nameList[loop][1])

nameList = [["Matthew","Reid"]]
numNames = int(input("How many names do you wish to add?"))
for names in range(numNames):
  newForename = str(input("Please enter a forename"))
  newSurname = str(input("Please enter a surname"))
  nameList.append([newForename, newSurname])

displayNames(nameList)