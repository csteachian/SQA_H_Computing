# 1204 Example 2

# A university needs to store details of each student,
# including their student ID, full name, age, and enrollment
# status (e.g., full-time or part-time).

# Identify the most appropriate data types and structures
# for each piece of information.

# SQA Reference Language
    # RECORD Student IS {
    # INTEGER studentID,
    # STRING fullName,
    # INTEGER age,
    # STRING enrollmentStatus
    # }

from dataclasses import dataclass
@dataclass
class student:
    studentID : int = 0
    fullName : str = ''
    age : int = 0
    enrollmentStatus : str = ''