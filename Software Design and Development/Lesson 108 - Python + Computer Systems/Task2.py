
def getValidNo(min, max):
    # getting valid integer min - max
    message = "Enter a denary number between " + str(min) + " and " + str(max) + ": "
    denaryNo = int(input(message))
    while denaryNo < min or denaryNo > max:
        print("Error!")
        denaryNo = int(input(message))
    return denaryNo

def workOutPositiveBinary(denaryNo):
    output = ""
    divisor = 128
    while divisor >= 1:
        if denaryNo >= divisor:
            output = output + "1"
            denaryNo = denaryNo - divisor
        else:
            output = output + "0"
        divisor = divisor // 2
    return output

def flipBinaryDigits(positiveNo):
    output = ""
    for x in range(len(positiveNo)):
        if positiveNo[x] == "1":
            output = output + "0"
        else:
            output = output + "1"
    return output

def addOneToBinary(flippedNo):
    counter = 1
    output = ""
    for x in range(len(flippedNo)-1,-1,-1):
        if flippedNo[x] == "1" and counter == 1:
            output = "0" + output
            counter = 1
        elif flippedNo[x] == "1" and counter == 0:
            output = "1" + output
        elif flippedNo[x] == "0" and counter == 1:
            output = "1" + output
            counter = 0
        elif flippedNo[x] == "0" and counter == 0:
            output = "0" + output
    return output

## main program
denaryNo = getValidNo(-128, -1)
positiveNo = workOutPositiveBinary((denaryNo*-1))
print(positiveNo)
flippedNo = flipBinaryDigits(positiveNo)
print(flippedNo)
result = addOneToBinary(flippedNo)
print(result)
