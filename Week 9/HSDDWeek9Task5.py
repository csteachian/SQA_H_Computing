'''
This code reflects the design we worked through on the board
'''

search_list = [4,12,5,8,2,6]
max = search_list[0]
for index in range(1,len(search_list)):
  if search_list[index] > max:
    max = search_list[index]
print(max)