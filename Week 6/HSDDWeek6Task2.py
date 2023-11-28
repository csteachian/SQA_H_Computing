# Program 2 - Predict and read

firstname = input("Enter your first name")
surname = input("Enter your surname")

print("Your first name is: ",firstname.upper())
print("Your surname is: ",surname.lower())
letters = len(firstname) + len(surname)
print("You have",str(letters),"letters in your name.")
init = ord(surname[0])
print("The first letter of your surname (",surname[0],") is ascii code ",init)
character = chr(init+1)
print("The next character after",surname[0],"in the alphabet is",character)