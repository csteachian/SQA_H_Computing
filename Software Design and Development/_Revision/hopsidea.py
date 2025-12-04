#-------------Main Program-----------------
#open file
total = 0
with open("Software Design and Development/_Revision/hopsidea.txt") as readfile:
    #filecontents = readfile.read()
    nextLine = readfile.readline()
    while nextLine != "":
        currentItem = nextLine.split(",")
        print("**"+currentItem[1].strip()+"**") # this is good for debugging issues
        if currentItem[1].strip() == "true":
            total = total + 1
        #print(nextLine.strip())
        nextLine = readfile.readline()

print("The total number of things that Hop suggested is: "+str(total))