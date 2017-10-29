import pygame, sys
from pygame.locals import *
import lib.game
import lib.hot_spots

pygame.init()

myHotspots = lib.hot_spots
myGame = lib.game


file = "resources/spots.csv"
hot_spots = myHotspots.Hotspots(file)
spot_descriptions = hot_spots.get_spot_names()
squares_to_move = hot_spots.get_squares_to_move()

player_one = myGame.Game("Player 1")
player_two = myGame.Game("Player 2")
players = []
players.append(player_one)
players.append(player_two)

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
black = (0,0,0)
pink = (255,200,200)

done = False
clock = pygame.time.Clock()

class Checkerboard(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Checkboard game')
        self.screen = pygame.display.set_mode((800,600), 0, 32)
        self.screen.fill((white))
        pygame.display.update()

    def forty_nine_squares(self):
        squares = [49, 48, 47, 46, 45, 44, 43]
        squares.extend([36, 37, 38, 39, 40, 41, 42])
        squares.extend([35, 34, 33, 32, 31, 30, 29])
        squares.extend([22, 23, 24, 25, 26, 27, 28])
        squares.extend([21, 20, 19, 18, 17, 16, 15])
        squares.extend([8, 9, 10, 11, 12, 13, 14])
        squares.extend([7, 6, 5, 4, 3, 2, 1])
        return squares

    def set_square_fill_color(self, player_1_position, player_2_position, hotspots, current_square):

        if player_1_position == player_2_position and current_square == player_1_position:
            color = pink
        elif player_1_position == current_square:
            color = blue
        elif player_2_position == current_square:
            color = darkBlue
        elif str(current_square) in hotspots:
            steps = int(hotspots.get(str(current_square)))
            if steps < 0:
                color = red
            else:
                color = green
        else:
            color = black
        return color

    def set_text_color(selfself,backgound_color):

        if backgound_color == black or backgound_color == red:
            color = white
        else:
            color = black
        return color

    def draw_checker_board(self, player_1_position, player_2_position, hotspots):
        x = 50
        y = 50
        column = 0
        squares = self.forty_nine_squares()
        for square in squares:
            if column % 7 == 0: #drawn 7 squares, need to start new row
                y += 33 # cell height 32, board 1
                x = 50 # reset x to left
            else:
                x += 33
            tx = x + 3
            ty = y + 3
            number = format(square, '02d')
            fill_color = self.set_square_fill_color(player_1_position, player_2_position, hotspots, square)
            font_color = self.set_text_color(fill_color)

            self.rect = pygame.draw.rect(self.screen, fill_color, (x, y, 32, 32))
            self.screen.blit(self.font.render(str(number), True, font_color), (tx, ty))

            column += 1
        pygame.display.update()

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()


def play(board):
    position1 = 1
    position2 = 1
    for player in players:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.event.wait()

        sum = player.roll()
        player.move(sum)

        position = player.get_position()

        if str(position) in squares_to_move:
            additional_steps = squares_to_move.get(str(position))
            player.move(int(additional_steps))

        if player == player_one:
            position1 = position

        if player == player_two:
            position2 = position

        board.draw_checker_board(position1, position2, squares_to_move)
        pygame.event.wait()

        print("p1 "+str(position1))
        print("p2 "+str(position2))
        print("winner "+str(player.check_winner()))

        if player.check_winner():
            return True

def main():
    board = Checkerboard()

    gameOver = False

    while not gameOver:
        # This limits the while loop to a max of 10 times per second.
        clock.tick(10)

        board.draw_checker_board(1, 1, squares_to_move)
        gameOver = play(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = False
                pygame.quit()
                sys.exit()


if __name__ == '__main__':
    main()