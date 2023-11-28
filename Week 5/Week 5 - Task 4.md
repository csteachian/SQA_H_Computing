# Week 5 - Task 4

Look at the following code

```python:
rightnumber = 8
guess = 1
number = int(input("Guess a number: "))
while (guess < 3) and (number != rightnumber):
  print("Not right. Try again.")
  number = int(input("Guess a number: "))
  guess = guess + 1

```

Investigate the code and then modify it so that the game allows 5 guesses instead of three.

**Bonus points if you can get it to display a "well done" message at the end of the game IF they guessed the number correctly.**

Remember to click on the `submit project` button in the top right of this Repl.
