# Higher Computing Science
# Software Design and Development
# Coursework 2010

product_name = []
stock_level = []
product_code = []

def enter_and_store_product_names_and_stock_levels(product_name, stock_level):
    for index in range(5):
        thisProduct = input("Please enter the product name: ")
        thisStockLevel = int(input("Please enter the stock level: "))
        product_name.append(thisProduct)
        stock_level.append(thisStockLevel)
    return product_name, stock_level

def calculate_and_store_product_codes(product_name, stock_level):
    for index in range(5):
        firstThree = product_name[index][0:3]
        lastThree = product_name[index][-3:]
        thisProductCode = firstThree + lastThree
        product_code.append(thisProductCode)
    return product_code

def display_product_names_and_codes(product_name, stock_level, product_code):
    print("| {:<15} | {:^15} | {:>20} |".format("Product Name","Product Code","Initial Stock Level"))
    print("="*60)
    for index in range(5):
        print("| {:<15} | {:^15} | {:>20} |".format(product_name[index],product_code[index],stock_level[index]))
    print("="*60)

def display_menu():
    print("MENU")
    print("====")
    print("F. Find a product")
    print("P. Purchase an item")
    print("Q. Quit")
    print()

def get_option():
    option = input("Enter menu option: ")
    while option.upper() not in ["F","P","Q"]:
        print("Invalid menu option!")
        option = input("Enter menu option: ")
    return option

def find_a_product(product_name, product_code, stock_level):
    target = input("Please enter product to be found: ")
    found = False
    for index in range(5):
        if product_code[index].upper() == target.upper():
            print("| {:<15} | {:^15} | {:>15} |".format("Product Name","Product Code","Stock Level"))
            print("="*55)
            print("| {:<15} | {:^15} | {:>15} |".format(product_name[index],product_code[index],stock_level[index]))
            print("="*55)
            found = True
    if found == False:
        print("Product not found.")

def purchase_a_product(product_name, product_code, stock_level):
    target = input("Please enter product to be purchased: ")
    found = False
    for index in range(5):
        if product_code[index].upper() == target.upper():
            print("| {:<15} | {:^15} | {:>15} |".format("Product Name","Product Code","Status"))
            print("="*55)
            status = "Out of stock"
            if stock_level[index] > 0:
                status = "In stock"
            print("| {:<15} | {:^15} | {:>15} |".format(product_name[index],product_code[index],status))
            print("="*55)
            if status == "In stock":
                print("Purchase confirmed")
                stock_level[index] = stock_level[index] - 1
            else:
                print("This product is out of stock.")
            found = True
                
    if found == False:
        print("Product not found.")
    return stock_level

def display_final_stock_check(product_name, product_code, stock_level):
    print("| {:<15} | {:^15} | {:^10} | {:10} |".format("Product Name","Product Code","Stock","Action"))
    print("="*63)
    for index in range(5):
        action = ""
        if stock_level[index] < 2:
            action = "Re-order"
        print("| {:<15} | {:^15} | {:^10} | {:10} |".format(product_name[index],product_code[index],stock_level[index],action))
    print("="*63)

# PSUEDOCODE
# 1. Enter and store product names and initial stock levels
product_name, stock_level = enter_and_store_product_names_and_stock_levels(product_name, stock_level)
# 2. Calculate and store product names
product_code = calculate_and_store_product_codes(product_name, stock_level)
# 3. Display product names and codes
display_product_names_and_codes(product_name, stock_level, product_code)
# 4. Start conditional loop
option = ""
while option.upper() != "Q":
# 5.    Display menu
    display_menu()
# 6.    Get option from user
    option = get_option()
# 7.    Where option if F, perform Find a product
    if option.upper() == "F":
        find_a_product(product_name, product_code, stock_level)
# 8.    Where option is P, perform Purchase a product
    if option.upper() == "P":
        stock_level = purchase_a_product(product_name, product_code, stock_level)
# 9.    Where option is Q, perform Quit
    if option.upper() == "Q":
        print("Quitting the program. Bye.")
# 10. End conditional loop when Q is chosen

# 11. Display final stock check
display_final_stock_check(product_name, product_code, stock_level)