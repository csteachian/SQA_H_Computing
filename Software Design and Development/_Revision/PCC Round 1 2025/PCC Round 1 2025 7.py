# Input a sequence of single characters, one per line, each A or B, to indicate a series of tennis points won in a single game.

# An input of A indicates that the server won the point, whilst B indicates that the receiver won the point.

# The scores in a game of tennis are awarded for each player as:
# 0, 15, 30, 40, game
# where each point won increases the player's score to the next score. 

# However if the score reaches 40-40, the game is said to be at deuce. 

# In this case, the player who wins the next point is said to be at advantage but does not immediately win the game.

# If the player with advantage wins the next point, they win the game otherwise the game returns to deuce.

# Output the number of deuces that occurred in the game.

# Input Format
# A sequence of single characters, one per line, each A or B

# Output Format
# A single non-negative whole number

# Example Input
# A
# A
# B
# A
# B
# B
# A
# B
# B
# A
# B
# B
# Example Output
# 3
# Example Explanation
# The game progressed as follows:
# 15-0, 30-0, 30-15, 40-15, 40-30, 40-40 (deuce), Advantage A, 40-40 (deuce), Advantage B, 40-40 (deuce), Advantage B, Game to B.

# In total there were 3 deuces so the output is 3.

# Constraints
# All input sequences will lead to a game win for one of the two players
# There will be a maximum of 10 deuces