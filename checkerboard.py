import lib.hot_spots
import lib.game
import lib.board
import random
import sys
import os

mySpots = lib.hot_spots
myGame = lib.game
myBoard = lib.board

file = "resources/spots.csv"
spots = mySpots.Spots(file)
spotNames = spots.getSpotNames()
spotSteps = spots.getSpotSteps()

player1 = myGame.Game("Player 1")
player2 = myGame.Game("Player 2")
players = []
players.append(player1)
players.append(player2)

red = "\033[0;37;41m"
green = "\033[0;37;42m"
normal = "\033[0;0;0m"
blue = "\033[0;37;44m"
purple = "\033[0;37;45m"
cyan = "\033[0;37;46m"


#myGrid.grid()
choosing = True
while choosing:
    ## Show menu ##
    print (22 * '-')
    print ("   G A M E - M E N U")
    print (22 * '-')
    print ("1. Play")
    print ("2. Exit")
    print (22 * '-')

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
            position1 = 1
            position2 = 1
            for player in players:
                if(player == player1):
                    print("\n" + blue + player.playerName + blue)
                else:
                    print("\n" + purple + player.playerName + purple)

                print(normal)

                #command = player.playerName + " please press 'p' to roll dice : "
                #raw_input(command)
                sum = player.roll()
                print("Previous position: " + str(player.playerPosition))
                print("Dice 1: " + str(player.roll1))
                print("Dice 2: " + str(player.roll2))
                print("Sum: " + str(sum))
                player.move(sum)
                print("New position: " + str(player.playerPosition))

                if str(player.playerPosition) in spotNames:
                    steps = spotSteps.get(str(player.playerPosition))
                    obs = spotNames.get(str(player.playerPosition))
                    if int(steps) < 0:
                        print("\033[0;37;41mOops! You have landed on obstacle " + obs + ". You will be moved backwards by " + steps + " steps\033[0;37;41m")
                        print("\033[0;0;0m")
                    else:
                        print("\033[0;37;42mCongratulations! You have landed on bonus " + obs + ". You will be moved forward by " + steps + " steps\033[0;37;42m")
                        print("\033[0;0;0m")
                    player.move(int(steps))
                    print("New position: " + str(player.playerPosition))

                if(player == player1):
                    position1 = player.playerPosition

                if(player == player2):
                    position2 = player.playerPosition
                myBoard.drawBoard(position1, position2, spotSteps)

                if player.victory == True:
                    gameOver = True
                    print("\n\033[0;37;42mGame over! Winner is " + player.playerName+"\033[0;37;42m")
                    print("\033[0;0;0m\n")
                    break

    elif choice == 2:
        print ("Bye!")
        sys.exit(0)
    else:
        print ("\n" * 50)
        print("I did not quite understand that")

