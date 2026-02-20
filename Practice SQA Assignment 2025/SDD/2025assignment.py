from dataclasses import dataclass
@dataclass
class order:
    orderNum : str = ""
    date : str = ""
    email : str = ""
    option : str = ""
    cost : float = 0.0
    rating : int = 0

path = "//albyn-sch/data/StaffHome/i.simpson/My Documents/Python/SQA_H_Computing/Practice SQA Assignment 2025/SDD/"

# Read from file into array  of records. 
def read_from_file():
    orders = [order() for index in range(505)]
    counter = 0
    with open(path+"orders.txt") as readfile:
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            orders[counter].orderNum = items[0]
            orders[counter].date = items[1]
            orders[counter].email = items[2]
            orders[counter].option = items[3]
            orders[counter].cost = float(items[4])
            orders[counter].rating = int(items[5])
            counter += 1
            line = readfile.readline().rstrip('\n')
    return orders

# Find the position of the customer who gave the first 5-star rating in a given month. 
def find_position(orders):
    position = -1
    return position

# Write details of the winning customer, or ‘no winner’ message, to a text file. 
def write_details(orders, position):
    with open(path+"winningCustomer.txt","w") as writefile:
        if position == -1:
            writefile.write("No winner")
        else:
            writefile.write(orders[position].orderNum+","+ 
                            orders[position].email+","+
                            str(orders[position].cost))

# Display the total number of orders delivered and the total number of orders collected. 
def display_totals(orders):
    pass

# main program


orders = read_from_file()
position = find_position(orders)
write_details(orders, position)
display_totals(orders)