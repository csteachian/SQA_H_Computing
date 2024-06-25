# 1. Create a program which asks the user to enter 5 temperatures, 
# then calculates and shows the average temperature rounded to 2 decimal places.
# You can choose to use 1D arrays or not for this challenge.

total = 0
for count in range(5):
    thisTemp = int(input("Please enter the next temperature: "))
    total = total + thisTemp
averageTemp = total / 5
print("The average temperature is",round(averageTemp,2))