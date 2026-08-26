# get character
character = input("Enter a character: ")
while len(character) != 1:
    print("NOOOOO. One character please.")
    character = input("Enter a character: ")
# convert character to ordinal value
ordValue = ord(character)
# output ordinal value
print("The character",character,"is ordinal value:",str(ordValue))