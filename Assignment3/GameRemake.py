
class Player:

    def __init__(self):
        self.score = 0

    def updateScore(self, addScore):
        self.score += addScore

    def playersScore(self):
        return self.score

class Game:
    
    def __init__(self):
        self.players = []

    def addPlayers(self, players):
        self.players.append(players)

class Application:
    pass