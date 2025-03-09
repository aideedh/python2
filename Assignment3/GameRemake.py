
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
        guess = random.randint(1,6)
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
            
            else:
                print("No one won!")
                break



    def getPlayerScore(self):
        # so this is to get the score of each player in list
        for players in self.players:
            print (f"{players.name} - Score: {players.playerScore()}")

class Application:

    gameStart = Game()
    playerOne = Player("playerOne")
    playerTwo = Player("playerTwo")
    playerThree = Player("playerThree")
    gameStart.addPlayers(playerOne)
    gameStart.addPlayers(playerTwo) 
    gameStart.addPlayers(playerThree)

    for loop in range(5):
        print(f"Staring round {loop}:")
        gameStart.match()
        
    print("------------------")
    print("Final Scores")
    print("------------------")

    gameStart.getPlayerScore()