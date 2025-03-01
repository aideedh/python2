from Player import Player

class Game():
    
    def __init__(self, players, guess):
        self.player = players
        self.guess = guess

    def start(self):
        self.guess = Player.roll()
        return self.guess

    def match(self):

