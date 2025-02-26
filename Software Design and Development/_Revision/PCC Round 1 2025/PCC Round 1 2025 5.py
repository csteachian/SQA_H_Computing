# An outline ASCII image can be made just using symbols for the outline and spaces elsewhere.

# For this batch of images, the first and last line must be entirely made of non-space symbols. The remaining lines must each contain exactly two non-space symbols, to mark the left and right side of the outline, but contain spaces for all other characters.

# Acceptable outline ASCII images, of a factory and a sand timer, are shown below.

# Input a single positive whole number to specify how many lines the image will contain. Then input that number of lines.

# Output the number of symbols, excluding spaces, that have been used to make the image.

# Input Format

# One line specifying a positive whole number n
# ... followed by n lines of text

# Output Format
# One positive whole number

# Example Input 1
# 6
# +-+
# | |
# |  \
# |   |
# |   |
# +---+
# Example Output
# 16
# Example Input 2
# 8
# +-------+
# \      /
#  \    /
#   \  /
#   /  \
#  /    \
# /      \
# +-------+
# Example Output 2
# 30