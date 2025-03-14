'''
Implement the following as version 3 and add the code to computer average score of all three players in 
problem 2.  
The average will be calculated and printed twice. Once using ‘/’ operator and then using ‘//’ operator.  
For example: 
 average1= (player1+ player2+player3)/3  # average using  ‘/’ operator
 average2= (player1+player2+player3)//3 # average using ‘//’ operator
Explain your observations. Remove the parenthesis from the equations and print average1 and average2 
again.  
Give screenshots of the code, outputs and the git repository

'''

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

# Get totak score of each player
print("---------------------------")
print(f"Player1 - Total Score = {scorePlayer1}")
print(f"Player2 - Total Score = {scorePlayer2}")
print(f"Player3 - Total Score = {scorePlayer3}")

# calculate avgs 

average1= (scorePlayer1+ scorePlayer2+scorePlayer3)/3  # average using  ‘/’ operator
average2= (scorePlayer1+scorePlayer2+scorePlayer3)//3 # average using ‘//’ operator

# Remove the parenthesis from the equations and print average1 and average2 

average4= scorePlayer1+scorePlayer2+scorePlayer3/3  # average using  ‘/’ operator
average5= scorePlayer1+scorePlayer2+scorePlayer3//3 # average using ‘//’ operator

# print the avgs
print("---------------------------")
print(" ") # this is a blank space
print("Average of roll 1 + roll 2:")
print(" ") # this is a blank space
print(f"average using  ‘/’ operator: {average1}")
print(f"average using ‘//’ operator: {average2}")
print(f"average using  ‘/’ operator - without (): {average4}")
print(f"average using ‘//’ operator - without (): {average5}")