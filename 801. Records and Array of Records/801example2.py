# 801. Records and Array of Records
# Example 2 - An array of records - Predict and Read

from dataclasses import dataclass
@dataclass
class person():
    height : float = 0.0
    weight : float = 0.0
    bmi : float = 0.0

BMIdetails = [person() for index in range(40)] # DECLARE BMIDetails(40) AS PERSON

BMIdetails[0].height  = 1.6
BMIdetails[0].weight  = 62.3
BMIdetails[0].bmi = BMIdetails[0].weight / (BMIdetails[0].height ** 2)

print(BMIdetails[0])

'''
(a) Why do we need the array element index in lines 13,14,15 and 17?
'''