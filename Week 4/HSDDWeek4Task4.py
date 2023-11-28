# Program 4 - Investigate and modify
age = float(input("Please enter your age: "))
if age > 0:
  print("You can see a U film.")
  if age >= 8:
    print("You can see a PG film.")
    if age >= 12:
      print("You can see a 12A film.")
      if age >= 15:
        print("You can see a 15 film.")