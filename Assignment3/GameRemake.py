
import random

class Player:

    def __init__(self):
        self.score = 0

    def updateScore(self, addScore):
        self.score += addScore

    def playersScore(self):
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
 
    def match(self):
        if self.players.roll() == self.players.guess():
            self.players.updateScore(1)
            print(f"{self.players} has matched, +1 point!")
        else:
            print("No one has matched! +0 points")

    def getPlayerScore(self):
        return self.players.playersScore()

class Application:

    gameStart = Game()
    playerOne = Player()
    playerTwo = Player()
    playerThree = Player()
    gameStart.addPlayers(playerOne)
    gameStart.addPlayers(playerTwo) 
    gameStart.addPlayers(playerThree)

    for loop in range(5):

        print(gameStart.players.roll())
