# Week 4 - Task 4

Look at the following code

```python:
age = float(input("Please enter your age: "))

if age < 0.0:
  print("Not possible! You have to be at least 0 years old.")
elif age < 15.0:
  print("You cannot apply to college yet.")
else:
  print("You can apply to college.")

```

Change the program so that it asks for the user's age but then tells them what film age ratings they are allowed to see at the cinema. For example:

```
Please enter your age: 4.0
You can go to see U or PG films at the cinema.
```

```
Please enter your age: 14.0
You can go to see U, PG or 12A films at the cinema.
```

Remember to click on the `submit project` button in the top right of this Repl.
