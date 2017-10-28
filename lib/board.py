from __future__ import print_function
import lib.colors

myColors = lib.colors
colors = myColors.Colors()

def Squares():
    squares = [49, 48, 47, 46, 45, 44, 43]
    squares.extend([36, 37, 38, 39, 40, 41, 42])
    squares.extend([35, 34, 33, 32, 31, 30, 29])
    squares.extend([22, 23, 24, 25, 26, 27, 28])
    squares.extend([21, 20, 19, 18, 17, 16, 15])
    squares.extend([8, 9, 10, 11, 12, 13, 14])
    squares.extend([7, 6, 5, 4, 3, 2, 1])
    return squares

def setColor(player1Position,player2Position,spots, currentCell):

    if player1Position == player2Position and currentCell == player1Position:
        colour = "cyan"
    elif player1Position == currentCell:
        colour = "blue"
    elif player2Position == currentCell:
        colour = "purple"
    elif str(currentCell) in spots and int(spots.get(str(currentCell))) < 0:
        colour = "red"
    elif str(currentCell) in spots and int(spots.get(str(currentCell))) > 0:
        colour = "green"
    else:
        colour = "normal"
    return colour

def drawBoard(player1Position, player2Position, spots):
    squares = Squares()

    i = 0
    for square in squares:
        number = format(square, '02d')
        cell_colour = setColor(player1Position, player2Position, spots, square)
        formatted_text = colors.format_text(cell_colour, number)
        normal_text = colors.format_text("normal", "")
        if i % 7 == 0:
            print("\n|", end='')
        print(formatted_text, end='')
        print(normal_text + "|", end='')
        i += 1

    print("\n")

