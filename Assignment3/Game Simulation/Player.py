import random

class Player():

    def __init__(self):
        self.scores = 0

    def roll(self):
        self.playerRoll = random.randint(1,6)
        return self.playerRoll
    
    def match(self):
