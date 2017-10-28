import random


class Game(object):
    name = ""
    position = 1
    double_dice = False
    first_roll = 0
    second_roll = 0
    winner = False

    def __init__(self, name):
        self.name = name
        self.position = 1

    def roll(self):
        self.double_dice = False
        self.first_roll = random.randint(1, 6)
        self.second_roll = random.randint(1, 6)
        sum = self.first_roll + self.second_roll

        if self.first_roll == self.second_roll:
            sum = -sum
            self.double_dice = True
        return sum

    def move(self, steps):
        self.position += steps

        if self.position <= 1:
            self.position = 1

        if self.position >= 49:
            self.position = 49
            self.winner = True

    def get_position(self):
        return self.position

    def check_winner(self):
        return self.winner