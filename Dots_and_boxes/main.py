from dots_and_boxes_game import *
from box import *


def main():
    game = DotsAndBoxesGame(5, 5, "A", "B")
    game.add_line(1,5,2,"A")
    game.add_line(1,5,0,"A")
    #game.add_line(1,5,2,"B")
    print(game)




main()