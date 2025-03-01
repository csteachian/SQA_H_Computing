# Everyone likes as many Saturdays as possible in a year.

# A year has 365 days unless it is a leap year which gives it an extra day.

# The number of Saturdays in a year can be calcuated from the day of the week which 1st January lies on and whether it is a leap year or not.

# Input the week day for January 1st in uppercase two letter format (MO / TU / WE / TH / FR / SA / SU).

# Also input whether it is a leap year or not as y (for yes) or n (for no).

# Output the number of Saturdays which that year will contain.

# Input Format
# A line specifying a week day using two uppercase letters
# A second line with a single character (y or n)

# Output Format
# One positive whole number

weekday = input("Enter the week day for January 1st (MO/TU/WE/TH/FR/SA/SU): ")
leapyear = input("Is it a leap year? (y/n): ")
if weekday == "SA":
    noSaturdays = 53
elif weekday == "FR" and leapyear == "y":
    noSaturdays = 53
else:
    noSaturdays = 52
print("There are",noSaturdays,"Saturdays this year.")