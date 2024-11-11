def info():
    age = int(input("Please enter your age: "))
    birth = int(input("Please enter the year you were born: "))
    print (age)
    return (age, birth)

def display(name, age, birth):
    print("Your name: ", name)
    print("Your age: ", age)
    print("Your year of birth: ", birth)

#Main Program
name = input("Please enter your name: ")
age, birth = info()
display(name, age, birth)
