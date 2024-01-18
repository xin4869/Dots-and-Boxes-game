from box import *


class DotsAndBoxesGame:
    TIE = "tie"
    PLAYER1 = "A"
    PLAYER2 = "B"

    def __init__(self, grid_width, grid_height, player_name_1, player_name_2):
        self.__grid_width = grid_width
        self.__grid_height = grid_height
        self.__player_name_1 = player_name_1
        self.__player_name_2 = player_name_2
        self.__grid = self.create_grid()

    def create_grid(self):
        grid = []
        for i in range(self.__grid_height):
            row = []
            for j in range(self.__grid_width):
                box = Box()
                row.append(box)
            grid.append(row)
        return grid

    def add_line(self, x, y, side, player):
        box = self.__grid[x-1][y-1]
        line = box.add_line(side)
        four_line = False

        if line:
            self.update_neighbour_of_box(x-1, y-1, side)
            if player == self.__player_name_1:
                owner = self.PLAYER1
            elif player == self.__player_name_2:
                owner = self.PLAYER2

            if box.four_lines_placed():
                box.add_owner(owner)
                four_line = True

            neighbour = self.get_neighbour_on_side(side, x-1, y-1)
            if neighbour is not None:
                if neighbour.four_lines_placed():
                    if neighbour.get_owner() is None:
                        neighbour.add_owner(owner)
                        four_line = True

        return line, four_line

    def update_neighbour_of_box(self, row_index, column_index, side):

        neighbour = self.get_neighbour_on_side(side, row_index, column_index)
        if neighbour is not None:
            if side == Box.DOWN:
                neighbour.add_line(Box.UP)
            elif side == Box.UP:
                neighbour.add_line(Box.DOWN)
            elif side == Box.RIGHT:
                neighbour.add_line(Box.LEFT)
            elif side == Box.LEFT:
                neighbour.add_line(Box.RIGHT)

    def get_neighbour_on_side(self, side, row_index, column_index):
        if side == Box.LEFT and column_index > 0:
            neighbour_box = self.__grid[row_index][column_index - 1]
        elif side == Box.RIGHT and column_index < self.__grid_width - 1:
            neighbour_box = self.__grid[row_index][column_index + 1]
        elif side == Box.DOWN and row_index < self.__grid_height - 1:
            neighbour_box = self.__grid[row_index + 1][column_index]
        elif side == Box.UP and row_index > 0:
            neighbour_box = self.__grid[row_index - 1][column_index]
        else:
            return None
        return neighbour_box

    def calculate_points_of_player(self, player):
        player_points = 0
        for i in range(self.__grid_height):
            for j in range(self.__grid_width):
                box = self.__grid[i][j]
                if box.get_owner() == player:
                    player_points += 1
        return player_points

    def is_ended(self):
        is_ended = True
        for i in range(self.__grid_height):
            for j in range(self.__grid_width):
                box = self.__grid[i][j]
                if box.get_owner() is None:
                    is_ended = False
        return is_ended

    def winner(self):
        player1_point = self.calculate_points_of_player(self.__player_name_1)
        player2_point = self.calculate_points_of_player(self.__player_name_2)

        if player2_point > player1_point:
            winner = self.__player_name_2
        elif player2_point < player1_point:
            winner = self.__player_name_1
        else:
            winner = self.TIE

        return winner

    def give_score(self):
        str = "\nScore:\n\n"
        str += f"{self.__player_name_1 + ' ('+ self.PLAYER1 + ')':<15}"
        str += " | "
        str += f"{self.__player_name_2 + ' ('+ self.PLAYER2 + ')':<15}"
        str += "\n-------------------------------------\n"
        str += f"{self.calculate_points_of_player(self.PLAYER1):<15}"
        str += " | "
        str += f"{self.calculate_points_of_player(self.PLAYER2):<15}\n"

        return str

    def one_row_of_grid(self, row_index):

        if row_index % 2 == 0:
            str = "   "
            for i in range(self.__grid_width):
                str += "o"
                if row_index == 0:
                    box = self.__grid[0][i]
                    has_line = box.has_line_on_side(1)
                elif row_index > 0:
                    box = self.__grid[int(row_index/2)-1][i]
                    has_line = box.has_line_on_side(3)

                if has_line:
                    str += " —— "
                else:
                    str += "    "
            str += "o"

        elif row_index % 2 != 0:
            str = ""
            for i in range(self.__grid_width):
                box = self.__grid[int((row_index+1)/2)-1][i]

                if box.has_line_on_side(0) and box.four_lines_placed() is False:
                    str += "|    "
                elif box.has_line_on_side(0) and box.four_lines_placed():
                    str += "| " + box.get_owner() + "  "
                else:
                    str += "     "

                if i == self.__grid_width - 1:
                    if box.has_line_on_side(2):
                        str += "|"
        return str


    def __str__(self):
        str = "      "
        for i in range(self.__grid_width):
            str += f"{i+1:<5d}"

        total_lines = 2 * self.__grid_height + 1
        for j in range(total_lines):
            if j % 2 == 0:
                str += f"\n{self.one_row_of_grid(j)}"
            elif j % 2 != 0:
                str += f"\n{int((j+1)/2):<3d}"
                str += f"{self.one_row_of_grid(j)}"

        str += f"\n{self.give_score()}"

        return str









