# At the local PackingTins4U factory, tin cans are usually packed in squares of size x by x cans for efficiency with just one can high.

# However, if x is a single digit, then sometimes the factory runs a special offer by adding a certain number of additional rows of cans for free to make a rectangle pack of dimensions x + a cans along by x cans wide.

# First input x, the length of the square packs being made.

# If and only if relevant, also input whether a special offer is running which will be indicated by a y for special offer and n for no special offer.

# If and only if it is a special offer, also input a, the number of additional rows which are being included for free. This input will only be available if there is a special offer running.

# Output the number of tin cans that each pack will contain.

# Input Format
# One line specifying a positive whole number x
# ... on some occasions followed by a second line of a single character (y or n)
# ... and on some occasions a third line specifying a positive whole number a

# Output Format
# One positive whole number

lengthOfSquarePacks = int(input("Enter the length of square packs being made: "))
widthOfSquarePacks = lengthOfSquarePacks
if lengthOfSquarePacks > 0 and lengthOfSquarePacks < 10:
    specialOffer = input("Is a special offer running? (y/n): ")
    if specialOffer == "y":
        additionalRows = int(input("Please enter the number of additional rows included for free: "))
        widthOfSquarePacks = widthOfSquarePacks + additionalRows
totalNumberOfCans = lengthOfSquarePacks * widthOfSquarePacks
print("The number of cans in the pack is: "+str(totalNumberOfCans))
    