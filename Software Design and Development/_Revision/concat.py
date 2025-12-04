fn = input("Enter first name:")
sn = input("Enter surname:")
fc = input("Enter form class:")
pwd = fn[0:3] + sn[-3:] + fc[1:]
print(pwd)