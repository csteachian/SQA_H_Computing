# getting valid integer 0 - 255
denaryNo = int(input("Enter a denary number between 0 and 255: "))
while denaryNo < 0 or denaryNo > 255:
    print("Error!")
    denaryNo = int(input("Enter a denary number between 0 and 255: "))
#
output = ""
divisor = 128
while divisor >= 1:
    if denaryNo >= divisor:
        output = output + "1"
        denaryNo = denaryNo - divisor
    else:
        output = output + "0"
    divisor = divisor // 2
print(output)
    