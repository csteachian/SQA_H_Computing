# ALGORITHM FOR TWO'S complement
# 1. Write down positive binary version of number
# 2. Invert all the bits
# 3. Add on one
# LITTLE TEST FOR VSCODE.DEV


# Define a function to convert a negative integer between -128 and # -1 into an 8-bit Two's Complement binary number
def IntegerToTwos(dec):
      # assign empty string for result
      twos = ''
      # convert n to binary and ignore the leading '0b'
      binary = bin(dec)[3:]     
      # add on leading 0s to make up to 8 bits in length
      binary = '0'*(8-len(binary)) + binary
      # print out the integer n
      print('\nDecimal:\t',dec)
      # print out the binary string
      print('Binary:\t',binary)
      # loop through each bit in binary string
      for bit in binary:
          # Invert each bit
          if bit == '0':
              twos += '1'
          else:
              twos += '0'
      # print one's complement
      print('Flip:\t',twos)
      # add on one to result (in decimal)
      addone = int(twos,base=2) + 1
      # convert back to binary and ignore leading '0b'
      twos = bin(addone)[2:]
      print('Add 1:\t',twos)
      # return two's complement string
      return twos

# Define a function to convert an 8-bit two's complement 
# binary string into a decimal integer
def TwosToInteger(binary):
    pass
    # Make decimal result = value of msb
    # For each remaining bit of binary String 
    # Add on value of this bit to result
    # print summary of this conversion
    # return result

# Main program
number = int(input('Enter a number between -128 and -1: '))
while (number < -128) or (number > -1):
  print("Error. I'll only accept numbers between -128 and -1.")
  number = int(input('Enter a number between -128 and -1: '))
  
binary = IntegerToTwos(number)
print('\nThe two\'s complement of {} is {}'.format(number,binary))

