#2019 Q11

from dataclasses import dataclass
@dataclass

class carData():
    #declares the record called CarData which can store the speed (MPH), acceleration(%), brake(%) and if the seatbelt is on or off
    speed:float
    acc:int
    brake:int
    seatBelt:bool

    #In pseudocode
    #
    #Record CarData:
    #   speed:real
    #   acc:integer
    #   brake:integer
    #   seatBelt:boolean
    #End Record


    #Declare a car as a record with data
    #
    #Declare car as CarData
    #car.speed=70
    #car.acc=20
    #car.brake=10
    #car.seatBelt=True
    

def createArray():
    readings = [carData(0.0,0,0,False) for x in range (200)]


    #In pseudocode
    #
    # Declare readings(200) as CarData
    #
    
    return readings

def fillArrayWithData(readings):
    import random
    for i in range(200):
        
        #random int for speed from 0-155 mph
        readings[i].speed = random.randint(0,155)
        
        #random int for braking percentage 0 to 100
        readings[i].acc = random.randint(0,100)

        #random int for break percentage 0 to 100
        readings[i].brake = random.randint(0,100)

        #random choice for seatbelt on (True) or off (False)
        readings[i].seatBelt = random.choice([True,False])
    return readings
        
def findMax(readings):
    maxSpeed = readings[0].speed
    for i in range (1,200):
        if readings[i].speed > maxSpeed:
            maxSpeed = readings[i].speed
    return maxSpeed

def countOccurrenceMaxSpeed(readings, maxSpeed):
    numberofcars = 0
    positions=[]
    for i in range(200):
        if readings[i].speed == maxSpeed:
            numberofcars+=1
            positions.append(i)
    return numberofcars, positions
            

def main():
    #mainProgram

    #calls the procedure createArray for create an array called readings which will hold 200 records of car data
    readings = createArray()

    #print the array of records to show they have been created (with default values)
    print(readings)
    print("------------------------------------------")

    #pass our array of records into a procedure to fill it with random values between limits that we can set (SQA assignments would give you a data file to read in)
    readings = fillArrayWithData(readings)

    #print the array to show it has been filled with random data
    print(readings)
    print("------------------------------------------")


    #call the procedure to find the highest speed from the car readings data
    maxSpeed = findMax(readings)

    #print the result of the highest speed
    print("The highest speed recorded was",maxSpeed)

    #extension
    #if we wanted to find out how many cars had the max speed, we could run another procedure using the count occurrence standard algorithm, and list the car numbers (from the array of records) that had this speed
    numberofcars, positions = countOccurrenceMaxSpeed(readings, maxSpeed)

    #print the results of the number of cards with the maz speed, and where they were found in the array
    print("The number of cars with the max speed reading was",numberofcars)
    print("Cars at position(s)",positions," recorded this speed")

#call the main procedure
main()
