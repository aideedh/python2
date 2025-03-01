import random

class Player():

    def __init__(self, scores):
        self.scores = scores


    def roll(self):
        roll = random.randint(1,6)
        return roll