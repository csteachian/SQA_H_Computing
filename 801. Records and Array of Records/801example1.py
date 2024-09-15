# 801. Records and Array of Records
# Example 1 - A single record - Predict and Read

from dataclasses import dataclass
@dataclass
class person():
    height : float = 0.0
    weight : float = 0.0
    bmi : float = 0.0

BMIrecord = person() # DECLARE BMIrecord AS PERSON

BMIrecord.height  = 1.6
BMIrecord.weight  = 62.3
BMIrecord.bmi = BMIrecord.weight / (BMIrecord.height ** 2)

'''
(a) What will the value of bmi be when presented to the user?
'''

print(BMIrecord)