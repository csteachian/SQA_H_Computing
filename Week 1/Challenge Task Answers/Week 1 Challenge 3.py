# 3. Create a program which asks the user to enter the name of 5 runners
# and the time they took to run 100 m. Store each name and time in two separate 1D arrays.
# Use a fixed loop to display the name and time of each runner from the 1D arrays.

runnerName = []
runnerTime = []

for count in range(5):
    thisRunnerName = input("Please enter the runner name: ")
    thisRunnerTime = float(input("Please enter the time in seconds it took to run 100m: "))
    runnerName.append(thisRunnerName)
    runnerTime.append(thisRunnerTime)

for count in range(5):
    print("Runner",str(count+1),":",runnerName[count],"took",runnerTime[count],"seconds.")