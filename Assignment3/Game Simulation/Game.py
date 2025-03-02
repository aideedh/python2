from Player import Player

import random

class Game():
    
    def __init__(self):
        # This is a list []
        # with a for loop making 3 player objects
        self.player = [Player() for num in range (1,4)]  
        self.guess = 0

    def start(self):
        self.guess = random.randint(1,6)

    def match(self):


