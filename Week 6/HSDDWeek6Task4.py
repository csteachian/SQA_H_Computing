# Program 4 - Investigate and Modify

name = ['alice adams','ben brown','carol codd']
newname = []

for x in range(len(name)):
  initial = name[x][0]
  surname = name[x].split(' ')[1]
  print(initial,surname)

print(newname)