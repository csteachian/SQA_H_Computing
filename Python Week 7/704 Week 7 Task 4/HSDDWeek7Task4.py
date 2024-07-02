# Task 4 - Write modular code

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