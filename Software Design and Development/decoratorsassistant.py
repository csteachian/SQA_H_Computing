# Decorators Assistant

# subroutines
def get_user_inputs():
    l = int(input("Enter length:"))
    b = int(input("Enter breadth:"))
    h = int(input("Enter height:"))
    return l, b, h # returning values of l, b and h to the main program

def calculate_area(length, breadth, height): # passing in parameters length, breadth, height
    floor_area = length * breadth
    wall_area = ((length * height) * 2) + ((breadth * height) * 2)
    return floor_area, wall_area # returning values of floor_area and wall_area to main program

def calculate_requirements(floor_area, wall_area): # passing in parameters floor_area, wall_area
    width_of_carpet_tile = 0.5 # 50cm
    roll_coverage = 10 # 10m^2
    paint_coverage = 5 # 5m^2
    no_carpet_tiles = floor_area / (width_of_carpet_tile ** 2)
    no_rolls_wallpaper = wall_area / roll_coverage
    litres_paint = floor_area / paint_coverage
    return no_carpet_tiles, no_rolls_wallpaper, litres_paint # returning values of no_carpet_tiles, no_rolls_wallpaper, litres_paint to main program

def display_results(length, breadth, height, floor_area, wall_area, no_carpet_tiles, no_rolls_wallpaper, litres_paint):
    print("Decorators Assistant")
    print()
    print("You entered: length=",length,"| breadth=",breadth,"| height=",height)
    print("The floor area is",floor_area,"m^2")
    print("The wall area is",wall_area,"m^2")
    print("The number of carpet tiles needed is",no_carpet_tiles)
    print("The number of rolls of wallpaper needed is",no_rolls_wallpaper)
    print("The number of litres of paint needed is",litres_paint)
    # notice that this subroutine isn't returning anything!!

# main program
length, breadth, height = get_user_inputs()
floor_area, wall_area = calculate_area(length, breadth, height)
no_carpet_tiles, no_rolls_wallpaper, litres_paint = calculate_requirements(floor_area, wall_area)
display_results(length, breadth, height, floor_area, wall_area, no_carpet_tiles, no_rolls_wallpaper, litres_paint)