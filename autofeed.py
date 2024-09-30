def enter_valid_weight_of_food():
    '''
    1.1 totalWeight = 0
    1.2 start fixed loop 5 times
    1.3 enter the foodWeight
    1.4 while the foodWeight < 0 or foodWeight > 200
    1.5 display “Invalid, a single container can only hold up to 200g”
    1.6 re-enter the foodWeight
    1.7 end while
    1.8 totalWeight = totalWeight + foodWeight
    1.9 end fixed loop
    '''
    totalWeight = 0
    for index in range(5):
        foodWeight = int(input("Enter food weight:"))
        while foodWeight < 0 or foodWeight > 200:
            print("Invalid, a single container can only hold up to 200g")
            foodWeight = int(input("Enter food weight:"))
        totalWeight = totalWeight + foodWeight

def enter_size_of_dog():
    pass

def store_a_message():
    pass

def calc_avg_weight():
    pass

def display_output_messages():
    pass

# Main program
#1. Enter valid weight of food in each container and calculate total weight
enter_valid_weight_of_food()
#2. Enter size of dog
enter_size_of_dog()
#3. Store a message that states if the total weight of food is within the recommended range for the size of dog entered
store_a_message()
#4. Calculate average weight of food
calc_avg_weight()
#5. Display output messages
display_output_messages()
