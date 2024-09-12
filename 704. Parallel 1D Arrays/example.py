# 704. Parallel 1D Arrays
# Example: Python

travel_agent = ''                                           #SET travel_agent TO ' '
booking_number = 0                                          #SET booking number TO 0
dates = []                                                  #SET dates TO EMPTY ARRAY
travel_agent = input("Enter travel agent name: ")           #RECEIVE travel agent FROM (STRING) KEYBOARD
booking_number = int(input("Enter booking number: "))       #RECEIVE booking number FROM (INTEGER) KEYBOARD
for index in range(3):                                      #LOOP 3 TIMES
    date = input("Enter date of booking: ")                      #RECEIVE date FROM (STRING) KEYBOARD
    dates.append(date)                                           #ADD date no TO dates ARRAY
                                                            #END LOOP
print(travel_agent, booking_number)                         #DISPLAY travel_agent, booking number AND the contents of the dates ARRAY
for index in range(3):
    print(dates[index])