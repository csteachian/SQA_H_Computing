# Predict and Run - Task 2

def displayScoreData(scores):
  average = sum(scores)/len(scores)
  print("Average score:",round(average,1))
  print("Scores ranged from:")
  print(min(scores),"to",max(scores))

# Main program
scores = [4,6,8,5,6,3,5,9,10,2,4,6,3,5]
displayScoreData(scores)
scores = [50,51,52,56,59,68]
displayScoreData(scores)

