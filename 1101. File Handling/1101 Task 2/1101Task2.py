#-------------Main Program-----------------
import time
#open file
with open("1101. File Handling/1101 Task 2/newfile.txt","w") as writefile:
    writefile.write("Python is great fun")
    time.sleep(1)

# Run the program and see what it does, then adapt the code so that the program writes your full name, favourite colour and birth month to the file instead.