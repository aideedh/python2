
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
        diceRoll = random.randint(1,6)
        return diceRoll

class Game:
    
    def __init__(self):
        self.players = []

    def addPlayers(self, players):
        self.players.append(players)

    def guess(self):
        playerGuess = random.randint(1,6)
        return playerGuess
 

    # def match(self):
    #     if self.players.roll() == self.players.guess():
    #         self.players.updateScore(1)
    #         print(f"{self.players} has matched, +1 point!")
    #     else:
    #         print("No one has matched! +0 points")


    def match(self):
        
        # itterate over every player

        for player in self.players:

            roll = player.roll()
            guess = player.guess()

            if roll == guess:
                




    def getPlayerScore(self):
        # so this is to get the score of each player in list
        for players in self.players:
            return players.playerScore()

class Application:

    gameStart = Game()
    playerOne = Player()
    playerTwo = Player()
    playerThree = Player()
    gameStart.addPlayers(playerOne)
    gameStart.addPlayers(playerTwo) 
    gameStart.addPlayers(playerThree)

    # for loop in range(5):

    #     print(gameStart.players.roll())
