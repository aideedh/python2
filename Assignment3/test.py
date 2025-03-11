import random

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def addScore(self, points):
        self.score += points

    def showScore(self):
        return self.score

    def roll(self):
        return random.randint(1,6)

class Game:
    
    def __init__(self, players = []):
            self.player = players
            self.guess = 0

    def start(self):
        self.guess = random.randint(1,6)
        return self.guess
    
    def match(self):

        #check if winner
        winner = False

        # ensure every guess is different per round
        guess = self.start()
        for player in self.player:
            # every player rolls a different number
            roll = player.roll()
    
            if roll == guess:
                player.addScore(1)
                print(f"{player.name} got 1 point")
                winner = True
                continue
        
        if winner == False:
            print("No Winners this round")

    def display(self):
        
        for player in self.player:
            print(f"{player.name} got a score of : {player.showScore()}")

class App:
    
    game = Game([
        Player("bob"),
        Player("john"),
        Player("Ton")
    ])

    for loop in range(1,6):

        print(f"Srating Round: {loop}")
        game.match()
        print(" ")

    print("------------------")
    print("Final Scores:")
    game.display()
    print("------------------")



