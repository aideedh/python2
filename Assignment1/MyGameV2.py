'''
2.Use of Arithmetic Operators and Git repositories
Implement the following as version2 of problem 1 given in this document.
Suppose all players in problem1 roll the dice two times.  
The score of each player is the sum of the previous and current value on the dice. 
The program should print the highest score. Use comments and import statements wherever applicable. 
Provide screenshots of the code,  output and git repository

# '''

import random

# set up intial scores
scorePlayer1 = 0
scorePlayer2 = 0
scorePlayer3 = 0

# use a for loop to loop the amount of rolls "2"
for rolls in range (1,3): 

    # Randint will change every loop 
    rollPlayer1 = random.randint(1,6)
    rollPlayer2 = random.randint(1,6)
    rollPlayer3 = random.randint(1,6)

    # update the scores for every roll
    scorePlayer1+=rollPlayer1
    scorePlayer2+=rollPlayer2
    scorePlayer3+=rollPlayer3

    # print the score each roll
    print("---------------------------")
    print(f"Player1 Roll #{rolls} - Score = {rollPlayer1}")
    print(f"Player2 Roll #{rolls} - Score = {rollPlayer2}")
    print(f"Player3 Roll #{rolls} - Score = {rollPlayer3}")

# SCORE LOGIC - BELLOW

# highest score logic - set player1 as higest initially
higestScore = scorePlayer1

# check if player 2 has the higeest score and print
if (scorePlayer2 > scorePlayer1 and scorePlayer2 > scorePlayer3):
    higestScore = scorePlayer2
    print("---------------------------")
    print (f"Player2 had the highest score of: {higestScore}")

# check if player 3 has the higeest score and print
elif (scorePlayer3 > scorePlayer1 and scorePlayer3 > scorePlayer2):
    higestScore = scorePlayer3
    print("---------------------------")
    print (f"Player3 had the highest score of: {higestScore}")
    
# If nither player 2 or player 3 have the highest player 1 wins
else:
    print("---------------------------")
    print (f"Player1 had the highest score of: {higestScore}")