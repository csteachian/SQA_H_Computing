#-------------Main Program-----------------
#open file
total = 0
with open("Software Design and Development/_Revision/benstie.txt") as writefile:
    answer = input("Is Ben wearing a tie today? (Y/N): ")
    if answer == "Y":
        total = total + 1
    writefile.write(str(total))