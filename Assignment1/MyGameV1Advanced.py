"""
1. Use of Random and Math Module:
Write a  program in python to simulate a game called MyGame.py. 
In this game you will use three variables called player1, player2 and player3. 
Each player rolls a dice, which means that the variables are initialized with random 
integers ranging from 1 to 6. Compare the values of player1, player2 and player3 to find 
the highest value. Print that highest value. Use comments and import statements wherever 
applicable. Give screenshots of the code, output and git repository containing this program.
"""

import random

# assign a random value to all three players
player1 = random.randint(1, 6)
player2 = random.randint(1, 6)
player3 = random.randint(1, 6)

# print statments for rolls
print (f"Player1 Rolled: {player1}")
print (f"Player2 Rolled: {player2}")
print (f"Player3 Rolled: {player3}")

# Set highest roll
highestRoll = 0

# if 1 player has the highest roll


# check if player 2 greater than player 1 and 3 
if (player2 > player1 and player2 > player3):
    highestRoll = player2
    print (f"Player2 had the highest roll with: {highestRoll}")
# check if player 3 greater than player 1 and 2
elif (player3 > player1 and player3 > player2):
    highestRoll = player3
    print (f"Player3 had the highest roll with: {highestRoll}")
# check if player 1 greater than player 2 and 3
elif (player1 > player2 and player1 > player3):
    highestRoll = player1
    print (f"Player1 had the highest roll with: {highestRoll}")


# Tie between 2 players
# Note: It will check if 2 players are tied and if the 3rd player is not higher than the other 2 
# Basically checks if t scores are equal and if the 3rd score is not higher than both those score than tie

# if player 1 and 2 tie
elif (player1 == player2 and player3 < player1 and player3 < player2):
    highestRoll = player1
    print (f"Player 1 and 2 tied with the highest roll of: {highestRoll}")
# if player 1 and 3 tie
elif (player1 == player3 and player2 < player1 and player2 < player3):
    highestRoll = player1
    print (f"Player 1 and 3 tied with the highest roll of: {highestRoll}")
# if player 2 and 3 tie
elif (player2 == player3 and player1 < player2 and player1 < player3):
    highestRoll = player2
    print (f"Player 2 and 3 tied with the highest roll of: {highestRoll}")
