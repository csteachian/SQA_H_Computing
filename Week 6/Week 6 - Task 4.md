# Week 6 - Task 4

Look at the following code

```python:
name = ['alice adams','ben brown','carol codd']
newname = []

for x in range(len(name)):
  initial = name[x][0]
  surname = name[x].split(' ')[1]
  print(initial,surname)

print(newname)
```

Investigate the code and then modify it so that it capitalises the initial and first letter of the surname, then adds this to the newname array. For example:

```
A Adams
B Brown
C Codd
['A Adams','B Brown','C Codd']
```

Remember to click on the `submit project` button in the top right of this Repl.
