# Write code that finds the number of teams that have scored more than 60 goals
teams = ["Man Utd", "Man City", "Spurs", "Liverpool", "Chelsea", "Arsenal", "Newcastle"]
goalsScored = [63, 89, 65, 79, 59, 69, 35 ]

occurrences = 0
#Loop through every team
for i in range(len(teams)):
  if goalsScored[i] > 60:
    occurrences = occurrences + 1
    print (teams[i] +  " scored more than 60 goals")

#once the loop has finished, print the total number of teams that has scored more than 60
print (str(occurrences) + " teams have scored more than 60")