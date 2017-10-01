import lib.obstacles
import random
import lib.game
import sys
import os

file = "resources/obstacles.csv"
myObstacles = lib.obstacles.Obstacles(file)
myGame = lib.game

obstacleNames = myObstacles.getObstacleNames()
obstacleSpaces = myObstacles.getObstacleSpaces()
print(obstacleNames)
print(obstacleSpaces)

player1 = myGame.game("Player 1")
player2 = myGame.game("Player 2")

key = "32"
if key in obstacleNames:
    print(obstacleNames[key])

if key in obstacleSpaces:
    print(obstacleSpaces[key])

choosing = True
while choosing:
    ## Show menu ##
    print (30 * '-')
    print ("   G A M E - M E N U")
    print (30 * '-')
    print ("1. Play")
    print ("2. Exit")
    print (30 * '-')

    players = []
    ## Get input ###
    choice = input('Enter your choice [1-2] : ')

    ### Convert string to int type ##
    choice = int(choice)

    ### Take action as per selected menu-option ###
    if choice == 1:
        gameOver = False
        print ("Starting game...")
        choosing = False
        if random.randint(0, 2) == 1:
            players = [player1,player2]
            print("Player 1 has been randomly chosen to start")
        else:
            players = [player2,player1]
            print("Player 2 has been randomly chosen to start")

        while not gameOver:
            for player in players:
                player
                print("")
                gameOver = True

    elif choice == 2:
        print ("Bye!")
        sys.exit(0)
    else:
        print ("\n" * 50)
        print("I did not quite understand that")

