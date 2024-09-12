# 704. Example: Python

#SET travel_agent TO ' '
#SET booking number TO 0
#SET dates TO EMPTY ARRAY
#RECEIVE travel agent FROM (STRING) KEYBOARD
#RECEIVE booking number FROM (INTEGER) KEYBOARD
#LOOP 3 TIMES
     #RECEIVE date FROM (STRING) KEYBOARD
     #ADD date no TO dates ARRAY
#END LOOP
#DISPLAY travel_agent, booking number AND the contents of the dates ARRAY

travel_agent = ''
booking_number = 0
dates = []
travel_agent = input("Enter travel agent name: ")
booking_number = int(input("Enter booking number: "))
for index in range(3):
    date = input("Enter date of booking: ")
    dates.append(date)
print(travel_agent, booking_number)
for index in range(3):
    print(dates[index])