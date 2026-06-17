# Create a program to take in a valid denary number between 0 and 255, and display the appropriate 8-bit binary sequence.

inputnum = int(input("Enter a valid denary number between 0 and 255: "))
while inputnum < 0 or inputnum > 255:
    print("Oi. I said a valid number.")
    inputnum = int(input("Enter a valid denary number between 0 and 255: "))

currentCol = 128
currentNum = inputnum
output = ""
while (currentNum >= 0) and (currentCol >= 1):
    if (currentNum - currentCol) >= 0:
        output = output + "1"
        currentNum = currentNum - currentCol
    else:
        output = output + "0"
    currentCol = currentCol / 2

print(output)
