
'''

Object passed to another object using method:
------------------------------------------------
This way is using addplayers(self, player) method to pass object to object

'''


import random

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def updateScore(self, addScore):
        self.score += addScore

    def playerScore(self):
        return self.score
    
    def roll(self):
        diceRoll = random.randint(1,3)
        return diceRoll

class Game:
    
    def __init__(self):
        self.players = []

    def addPlayers(self, players):
        self.players.append(players)

    def guess(self):
        guess = random.randint(1,3)
        return guess

    def match(self):
        
        # itterate over every player

        for player in self.players:

            roll = player.roll()
            roundGuess = self.guess()

            # than check if players roll matched guess
            if roll == roundGuess:
                player.updateScore(1)
                print(f"{player.name} has matched, +1 point!")
                # after 1 player matches it moves to next itteration of loop instead of else statment
                continue
            
            else:
                print("No one won!")
                # this break is to stop it from repeating messege
                break

    def getPlayerScore(self):
        # so this is to get the score of each player in list
        for players in self.players:
            print (f"{players.name} - Score: {players.playerScore()}")

class Application:

    # creating instance of an object
    gameStart = Game()

    # creating player objects
    playerOne = Player("playerOne")
    playerTwo = Player("playerTwo")
    playerThree = Player("playerThree")

    # passing player objects to game object
    gameStart.addPlayers(playerOne)
    gameStart.addPlayers(playerTwo) 
    gameStart.addPlayers(playerThree)

    # running the game using match function 5 times
    for loop in range(1,6):
        print(f"Staring round {loop}:")
        gameStart.match()
    
    # finished
    print("------------------")
    print("Final Scores")
    print("------------------")
    gameStart.getPlayerScore()



'''

Object is an instance of another object:
------------------------------------------------
This was uses an instance of an object within another object

'''

import random

class Player:
    
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
    
    def roll(self):
        return random.randint(1,6)
    
    def playerScore(self):
        return self.score
    
    def updateScore(self, score):
        self.score += score


class Game:
    
    # object init with instance of another classes - object
    def __init__(self):
        self.players = [
            Player("playerOne", 0),
            Player("playerTwo", 0),
            Player("playerThree", 0)
        ]
        self.guess = int


    def start(self):
        self.guess = random.randint(1,6)
        return self.guess
        
    def match(self):

        # Bool for if any player matched
        check = False

        for player in self.players:

            guess = self.start()
            roll = player.roll()

            if roll == guess:
                player.updateScore(1)
                print(f"{player.name} has matched, +1 point!")
                check = True
                continue
        
        # if no player matched whan this will print during the round
        if check == False:
                print(f"No one won!")                

    def showScores(self):
        
        for players in self.players:
            print (f"{players.name} - Score: {players.playerScore()}")

class application:
    
    # instnce of game object
    game = Game()

    # loop the amount of time game will be played
    for loop in range(1,6):
        print("------------------")
        print(f"Staring round {loop}:")
        game.match()
    
    # Display final results
    print("------------------")
    print("Final Scores")
    print("-----------------------")
    game.showScores()
    print("-----------------------")