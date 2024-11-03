# 1204 Data Types and Structures
# Examples of use of data types and structures
# at National 5 and Higher level

# ==========
# National 5
# ==========

# character
initial = 'A'

# string
surname = 'Smith'

# numeric (integer and real)
age = 23
balance = 19.99

# Boolean
match = True

# 1-D arrays
marks = [43,76,47,64,86,29]

# =======
# Higher
# =======

# parallel 1-D arrays
firstName = ['Alice', 'Bob', 'Charlie']
surname = ['Smith', 'Jones', 'Good']
register = [True, True, False]

# records
from dataclasses import dataclass
@dataclass
class student:
    firstName : str = ''
    surname : str = ''
    register : bool = False

newStudent = student()
newStudent.firstName = 'Alice'
newStudent.surname = 'Smith'
newStudent.register = True

# arrays of records
classOne = [student() for index in range(20)]
classOne[0].firstName = 'Alice'
classOne[0].surname = 'Smith'
classOne[0].register = True