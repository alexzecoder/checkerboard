import lib.obstacles
import lib.game
import random
import sys
import os


myObstacles = lib.obstacles
myGame = lib.game

file = "resources/obstacles.csv"
obstacles = myObstacles.Obstacles(file)
obstacleNames = obstacles.getObstacleNames()
obstacleSpaces = obstacles.getObstacleSpaces()

player1 = myGame.Game("Player 1")
player2 = myGame.Game("Player 2")
players = []
players.append(player1)
players.append(player2)

choosing = True
while choosing:
    ## Show menu ##
    print (30 * '-')
    print ("   G A M E - M E N U")
    print (30 * '-')
    print ("1. Play")
    print ("2. Exit")
    print (30 * '-')

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
            print("\nPlayer 1 has been randomly chosen to start\n")
        else:
            print("Player 2 has been randomly chosen to start\n")
            players.reverse()

        while not gameOver:
            for player in players:
                print("\n" + player.playerName + " playing")
                #command = player.playerName + " please press 'p' to roll dice : "
                #raw_input(command)
                sum = player.roll()
                print("Previous position: " + str(player.playerPosition))
                print("Dice 1: " + str(player.roll1))
                print("Dice 2: " + str(player.roll2))
                print("Sum: " + str(sum))
                player.move(sum)
                print("New position: " + str(player.playerPosition))

                if str(player.playerPosition) in obstacleNames:
                    steps = obstacleSpaces.get(str(player.playerPosition))
                    obs = obstacleNames.get(str(player.playerPosition))
                    if int(steps) < 0:
                        print("Oops! You have landed on obstacle " + obs + ". You will be moved backwards by " + steps + " steps")
                    else:
                        print("Congratulations! You have landed on bonus " + obs + ". You will be moved forward by " + steps + " steps")
                    player.move(int(steps))

                if player.victory == True:
                    gameOver = True
                    print("\n\033[0;32;40mGame over! Winner is " + player.playerName+"\033[0;32;40m")
                    print "\n"
                    break

    elif choice == 2:
        print ("Bye!")
        sys.exit(0)
    else:
        print ("\n" * 50)
        print("I did not quite understand that")

