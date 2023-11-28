rightnumber = 8
guess = 1
number = int(input("Guess a number: "))
while (guess < 3) and (number != rightnumber):
  print("Not right. Try again.")
  number = int(input("Guess a number: "))
  guess = guess + 1