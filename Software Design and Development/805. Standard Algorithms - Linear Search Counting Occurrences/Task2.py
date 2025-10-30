# Create a program design (using Pseudocode)
# that will display the position in the list
# of the last user to purchase a hamster from
# the pet shop. Use the list below.


# PetPurchased
# 'Dog', 'Dog', 'Cat', 'Rabbit', 'Hamster', 'Cat',
# 'Hamster', 'Budgie'

PetPurchased = ['Dog', 'Dog', 'Cat', 'Rabbit', 'Hamster', 'Cat',
                'Hamster', 'Budgie']

# Linear search
target = "Hamster"
foundPosition = -1
for index in range(len(PetPurchased)):
    if PetPurchased[index] == target:
        foundPosition = index

if foundPosition != -1:
    print(f"The last instance of {target} was found at position {foundPosition}")
else:
    print(f"The target {target} was not found.")

# PSEUDOCODE
# 1. Set target to "Hamster"
# 2. Set foundPosition to -1
# 3. For index = 0 to len(PetPurchased) Do
# 4.    If PetPurchased[index] = target Then
# 5.        Set foundPosition to index
# 6.    End If
# 7. Next / End Loop
# 8. If foundPosition != -1 Then
# 9.    Display the position of the last instance of target
# 10. Else
# 11.   Display target not found
# 12. End If