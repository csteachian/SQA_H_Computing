# 1001Task4.py
# Standard Algorithms - Finding Min + Max

# Predict and run

search_list = [4,12,5,8,2,6]
max = search_list[0]
for index in range(1,len(search_list)):
  if search_list[index] > max:
    max = search_list[index]
print(max)