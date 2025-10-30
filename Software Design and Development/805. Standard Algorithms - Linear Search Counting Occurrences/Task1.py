# Create a program design (using Pseudocode)
# that will count and display the number of users
# that own an iPhone from the array below:

# OwnsAnIPhone
# Yes, No, No, No, Yes, Yes, Yes, Yes

ownsAnIPhone = [True, False, False, False, True,
                True, True, True]

count = 0
for index in range(len(ownsAnIPhone)):
    if ownsAnIPhone[index] == True:
        count += 1

print(f"There are {count} iPhones.")

# PSEUDOCODE
# 1. Set count to 0
# 2. For index = 0 to len(ownsAnIPhone) Do
# 3.    If ownsAnIPhone[index] = True Then
# 4.        Add 1 to count
# 5.    End If
# 6. Next / End Loop
# 7. Display number of iPhones found on the screen