
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

player1 = random.randint(1,6)
player2 = random.randint(1,6)
player3 = random.randint(1,6)

print (f"Player 1 rolled: {player1}")
print (f"Player 1 rolled: {player2}")
print (f"Player 1 rolled: {player3}")

maximum = max(player1, player2, player3)

print(f"The highest roll was: {maximum}")


