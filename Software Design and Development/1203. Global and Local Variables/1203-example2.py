def info():
    global age, birth
    age = int(input("Please enter your age: "))
    birth = int(input("Please enter the year you were born: "))
    print (age)

def display(name, age, birth):
    print("Your name: ", name)
    print("Your age: ", age)
    print("Your year of birth: ", birth)

#Main Program
age = 0
birth = 1900
name = input("Please enter your name: ")
info()
display(name, age, birth)
