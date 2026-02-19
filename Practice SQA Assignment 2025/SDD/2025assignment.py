
# Read from file into array  of records. 
def read_from_file():
    return orders

# Find the position of the customer who gave the first 5-star rating in a given month. 
def find_position(orders):
    return position

# Write details of the winning customer, or ‘no winner’ message, to a text file. 
def write_details(orders, position):
    pass

# Display the total number of orders delivered and the total number of orders collected. 
def display_totals(orders):
    pass

# main program
orders = []
orders = read_from_file()
position = find_position(orders)
write_details(orders, position)
display_totals(orders)