from box import Box


class DotsAndBoxesGame:
    
    # This class represents a game of Dots and Boxes.

    TIE = "tie"
    PLAYER1 = "A"
    PLAYER2 = "B"

    def __init__(self, grid_width, grid_height, player_name_1, player_name_2):
        
        # This method initializes a game object. The attributes of the game object are:
        # - grid_width: given as a parameter, tells the width of the grid
        # - grid_height: given as a parameter, tells the height of the grid
        # - grid: a two dimensional list that consists of the box objects
        # - player_name_1: given as a parameter, the name of the first player (string)
        # - player_name_2: given as a parameter, the name of the second player (string)
        
        self.__grid_width = grid_width
        self.__grid_height = grid_height
        self.__grid = self.create_grid()
        self.__player_name_1 = player_name_1
        self.__player_name_2 = player_name_2

    def create_grid(self):
        
        # Method creates and returns the game grid. The grid consists of box objects.
        
        grid = []
        for i in range(self.__grid_height):
            row = []
            for j in range(self.__grid_width):
                box = Box()
                row.append(box)
            grid.append(row)
        return grid

    def add_line(self, x, y, side, player):  # row, column
        
        # This method adds one line to the grid. The parameters are the coordinates of the box (x, y)
        # (integers starting from 1), direction (integer between 0 to 3) and the player (string).
        # The line is added to the given side of the box. Method returns a tuple (boolean, boolean).
        # First return value is True if the line was added successfully.
        # The other return value is True if the added line was fourth line in the box or in its neighbour box.
        # Player earns a point from each completely bordered box.

        # This method also calls the method update_neighbour_of_box() to add the line to the neighbour box.
        
        box = self.__grid[x - 1][y - 1]
        four_lines_placed = False
        line_added = box.add_line(side)
        if line_added:
            self.update_neighbour_of_box(x - 1, y - 1, side)
            if player == self.__player_name_1:
                owner = self.PLAYER1
            else:
                owner = self.PLAYER2
            if box.four_lines_placed():
                box.add_owner(owner)
                four_lines_placed = True
            neighbour = self.get_neighbour_on_side(side, x - 1, y - 1)
            if neighbour is not None and neighbour.four_lines_placed() and neighbour.get_owner() is None:
                neighbour.add_owner(owner)
                four_lines_placed = True
        return line_added, four_lines_placed

    def update_neighbour_of_box(self, row_index, column_index, side):
        
        # Method adds a line to the side of the box's neighbour if there is neighbour in that side.
        # The coordinates of the box and the side are given as parameters (side is an integer between 0 to 3).
        
        neighbour = self.get_neighbour_on_side(side, row_index, column_index)
        if neighbour is not None:
            if side == Box.LEFT:
                neighbour.add_line(Box.RIGHT)
            elif side == Box.RIGHT:
                neighbour.add_line(Box.LEFT)
            elif side == Box.UP:
                neighbour.add_line(Box.DOWN)
            elif side == Box.DOWN:
                neighbour.add_line(Box.UP)

    def get_neighbour_on_side(self, side, row, column):
        
        # Method finds and returns the neighbour of the box on the side given as
        # a parameter. The coordinates of the box are given as parameters.
        
        if side == Box.LEFT and column - 1 >= 0:
            neighbour = self.__grid[row][column - 1]
        elif side == Box.RIGHT and column + 1 < self.__grid_width:
            neighbour = self.__grid[row][column + 1]
        elif side == Box.UP and row - 1 >= 0:
            neighbour = self.__grid[row - 1][column]
        elif side == Box.DOWN and row + 1 < self.__grid_height:
            neighbour = self.__grid[row + 1][column]
        else:
            neighbour = None
        return neighbour

    def calculate_points_of_player(self, player):
        
        # Calculates and returns the points of a player. The char ('A'/'B') corresponding
        # to the player is give as a parameter.
        
        points = 0
        for row in self.__grid:
            for box in row:
                if box.get_owner() == player:
                    points += 1
        return points

    def is_ended(self):
        
        # Method checks if the game is ended. The game ends when all boxes has an owner. Returns True/False.
        
        for row in self.__grid:
            for box in row:
                if box.get_owner() is None:
                    return False
        return True

    def winner(self):
        
        # Returns the player name (string) with more points. If the points are even, returns a string "tie".
        
        points1 = self.calculate_points_of_player(self.PLAYER1)
        points2 = self.calculate_points_of_player(self.PLAYER2)
        if points1 > points2:
            return self.__player_name_1
        elif points2 > points1:
            return self.__player_name_2
        else:
            return self.TIE

    def give_score(self):
        
        # Returns a string with the score of both players.
        
        string = "\nScore:\n"
        string += "\n{:<15s} | {:<15s}\n".format(self.__player_name_1 + " (A)", self.__player_name_2 + " (B)")
        string += "-" * 37
        string += "\n{:<15d} | {:<15d}\n".format(self.calculate_points_of_player(self.PLAYER1),
                                                 self.calculate_points_of_player(self.PLAYER2))
        return string

    def one_row_of_grid(self, row_index):
        
        # A helper method that returns a string containing one row of the grid. The index of the row
        # is given as a parameter.
        
        string = ""
        last_row = False
        row = row_index // 2
        for i in range(self.__grid_width):
            # Check if the row is the last one
            if row == self.__grid_height:
                box = self.__grid[row - 1][i]
                last_row = True
            else:
                box = self.__grid[row][i]
            if row_index % 2 == 0:
                if i == 0:
                    string += "   "
                string += "o "
                if not last_row and box.has_line_on_side(Box.UP):
                    string += "—— "
                elif last_row and box.has_line_on_side(Box.DOWN):
                    string += "—— "
                else:
                    string += "   "
                if i == self.__grid_width - 1:
                    string += "o"
            else:
                if box.has_line_on_side(Box.LEFT):
                    string += "| "
                else:
                    string += "  "
                if box.four_lines_placed():
                    string += "{:2s} ".format(box.get_owner())
                else:
                    string += "   "
                if i == self.__grid_width - 1 and box.has_line_on_side(Box.RIGHT):
                    string += "|"
        string += "\n"
        return string

    def __str__(self):
        
        # Returns a string that contains the current situation of the game grid.
        
        string = "   "
        for i in range(self.__grid_width):
            string += "   {:d} ".format(i + 1)
        string += "\n"
        for row in range(self.__grid_height * 2 + 1):
            if row % 2 == 1:
                string += "{:d}  ".format((row + 1) // 2)
            one_row = self.one_row_of_grid(row)
            string += one_row
        string += self.give_score()
        return string
