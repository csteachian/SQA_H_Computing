#-------------Main Program-----------------
#open file
import time
with open("Software Design and Development/1101. File Handling/1101 Task 1/SampleFile.txt") as readfile:
    #filecontents = readfile.read()
    nextLine = readfile.readline()
    while nextLine != "":
        print(nextLine.strip())
        time.sleep(2)
        nextLine = readfile.readline()