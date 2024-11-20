The modular code is:

```python:
def get_name():
  name = input("Enter your name")
  return name

def get_score():
  pass

def get_time():
  pass

def calc_bonus(time, score):
  pass

def calc_score(score, bonus):
  pass

def display_score(name, score):
  pass

# Main Program
n = get_name()
s = get_score()
t = get_time()
b = calc_bonus(t, s)
s = calc_score(s, b)
display_score(n, s)
```

# Task 4

Change the `pass` commands to appropriate code to implement the following pseudocode:

\*\* get_score

1. Ask the user to enter a score between 0 and 9999
2. Return score to the main program

\*\* get_time

1. Ask the user to enter a time in seconds between 1 and 400
2. Return time to the main program

\*\* calc_bonus

1. Work out the bonus score using the following calculation: bonus = (score % 11) \* time
2. Return bonus to the main program

\*\* calc_score

1. Set score to score + bonus
2. Return score to the main program

\*\* display_score

1. Display name and score on the screen
