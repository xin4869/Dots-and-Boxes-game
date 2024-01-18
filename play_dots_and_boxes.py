
from dots_and_boxes_game import DotsAndBoxesGame
from box import Box


def ask_coordinates(max_row, max_column):
   
    while True:
        print("Enter the coordinates of the box separated by comma (row,column):")
        coord_string = input()
        parts = coord_string.split(",")
        try:
            row = int(parts[0])
            column = int(parts[1])
            while row > max_row or row < 1 or column > max_column or column < 1:
                print("Coordinates are out of range.")
                print(f"A row coordinate has to be between 1 and {max_row}, and a column coordinate between 1 and {max_column}.")
                print("Enter the coordinates of the box separated by comma (row,column):")
                coord_string = input()
                parts = coord_string.split(",")
                row = int(parts[0])
                column = int(parts[1])
            return row, column
        except ValueError:
            print("Invalid input!")
            print("You need to give numbers separated by comma.")
        except IndexError:
            print("Invalid input!")
            print("Separate the coordinates with comma.")


def ask_direction():
  
    print("Enter the side of the box to where to place the line.")
    while True:
        print("Use the following letters: l, r, u, d")
        print("(l = LEFT, r = RIGHT, u = UP, d = DOWN):")
        letter = input()
        if letter.lower() == 'l':
            return Box.LEFT
        elif letter.lower() == 'u':
            return Box.UP
        elif letter.lower() == 'r':
            return Box.RIGHT
        elif letter.lower() == 'd':
            return Box.DOWN
        else:
            print("You entered wrong input.")


def ask_int():
    
    while True:
        try:
            integer = int(input())
            return integer
        except ValueError:
            print("Invalid integer! Enter a number again:")

def main():
    print("Welcome to play Dots and Boxes!")

    player1 = input("Enter the name of the first player:\n")
    player2 = input("Enter the name of the second player:\n")
    print("Enter the width of the grid:")
    width = ask_int()
    while width < 1:
        print("The width must be at least 1.")
        print("Enter the width of the grid:")
        width = ask_int()
    print("Enter the height of the grid:")
    height = ask_int()
    while height < 1:
        print("The height must be at least 1.")
        print("Enter the height of the grid:")
        height = ask_int()

    
    game = DotsAndBoxesGame(width, height, player1, player2)

    player = player1
    print(game)

    
    while not game.is_ended():
        print(f"It is {player}'s turn.")
        row, column = ask_coordinates(height, width)
        direction = ask_direction()

        
        line_added, point_earned = game.add_line(row, column, direction, player)
        while not line_added:
            print("There is already a line in that position. Give coordinates again.")
            row, column = ask_coordinates(height, width)
            direction = ask_direction()
            line_added, point_earned = game.add_line(row, column, direction, player)
        print(game)

        
        if point_earned:
            if game.is_ended():
                print(f"{player} earned a point.")
            else:
                print(f"{player} earned a point and takes another turn.")

        else:
            if player == player1:
                player = player2
            else:
                player = player1

    print("Game ended.")
    print(game.give_score())
    winner = game.winner()
    if winner == DotsAndBoxesGame.TIE:
        print("It is a tie.")
    else:
        print(f"The winner is {winner}!")
    print()
    print("Program ends.")


main()
