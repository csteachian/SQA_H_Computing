# A lot of action can occur in the second-half of a hockey match as teams get tired.

# Input the half-time score as 2 whole numbers on 2 separate lines.

# Input the full-time score as 2 whole numbers on 2 separate lines.

# Output the number of goals scored after the half-time break.

# Input Format
# Four lines each containing one non-negative whole number

# Output Format
# One non-negative whole number

homeHT = int(input("Enter the half time score for the home team: "))
awayHT = int(input("Enter the half time score for the away team: "))

print()

homeFT = int(input("Enter the full time score for the home team: "))
awayFT = int(input("Enter the full time score for the away team: "))

noGoalsScored = (homeFT + awayFT) - (homeHT + awayHT)

print("The number of goals scored after the half time break was: "+str(noGoalsScored))