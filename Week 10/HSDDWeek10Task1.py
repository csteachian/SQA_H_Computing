#-------------Main Program-----------------
#open file
with open("SampleFile.txt") as readfile:
    filecontents = readfile.read()
    print(filecontents)