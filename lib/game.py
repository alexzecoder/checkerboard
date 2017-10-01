import random
class game:
    playerName = ""
    playerPosition = 1
    doubleDice = False
    roll1 = 0
    roll2 = 0
    victory = False

    def __init__(self, name):
        self.playerName = name
        self.playerPosition = 1

    def roll(self):
     self.doubleDice = False
     self.roll1 = random.randint(0, 6)
     self.roll2 = random.randint(0, 6)
     sum = self.roll1 + self.roll2
     if self.roll1 == self.roll2:
        sum = -sum
        self.doubleDice = True
     return sum

    def move(self, steps):
        self.playerPosition += steps
        if self.playerPosition < 1:
            self.playerPosition = 1
        if self.playerPosition >= 49:
            self.playerPosition = 49
            self.victory = True
