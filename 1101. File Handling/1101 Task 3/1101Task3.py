items = []
names = []
marks = []
with open("pupils.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        names.append(items[0])
        marks.append(items[1])
        line = readfile.readline().rstrip('\n')
print(names)
print(marks)

# Run the program. Now edit the code so that it displays each student name with their mark e.g. Monica - 85