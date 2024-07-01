# Week 8 Task 1

## Predict and run

Look at the code in [main.py](../main.py)

```python:
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
```

Click to view the [predict.md](../predict.md) file and answer the questions **before** running the code.

Submit your project once you have added your answers.
