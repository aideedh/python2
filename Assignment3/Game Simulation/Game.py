from Player import Player

import random


class Game():
    
    def __init__(self):
        # This is a list []
        # with a for loop making 3 player objects
        p1 = Player()
        p2 = Player()
        p3 = Player()
        self.player = [p1,p2,p3]
        self.guess = 0



    def start(self):
        self.guess = random.randint(1,6)

    def match(self):


