# 801. Records and Array of Records
# Example 2 - An array of records - Predict and Read

from dataclasses import dataclass
@dataclass
class person():
    height : float = 0.0
    weight : float = 0.0
    bmi : float = 0.0

BMIdetails = [person() for index in range(40)] # DECLARE BMIDetails(40) AS PERSON

BMIdetails[0].height  = 1.75
BMIdetails[0].weight  = 70.5
BMIdetails[0].bmi = BMIdetails[0].weight / (BMIdetails[0].height ** 2)

BMIdetails[1].height  = 1.62
BMIdetails[1].weight  = 55.8
BMIdetails[1].bmi = BMIdetails[1].weight / (BMIdetails[1].height ** 2)

BMIdetails[2].height  = 1.88
BMIdetails[2].weight  = 95.2
BMIdetails[2].bmi = BMIdetails[2].weight / (BMIdetails[2].height ** 2)

BMIdetails[3].height  = 1.70
BMIdetails[3].weight  = 82.3
BMIdetails[3].bmi = BMIdetails[3].weight / (BMIdetails[3].height ** 2)

BMIdetails[4].height  = 1.80
BMIdetails[4].weight  = 68.0
BMIdetails[4].bmi = BMIdetails[4].weight / (BMIdetails[4].height ** 2)

print(BMIdetails[0])
print(BMIdetails[1])
print(BMIdetails[2])
print(BMIdetails[3])
print(BMIdetails[4])

'''
(a) Why do we need the array element index in lines 13,14,15 and 17?
'''