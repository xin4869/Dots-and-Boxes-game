class Box:
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

    def __init__(self):
        self.__owner = None
        self.__left_side = False
        self.__right_side = False
        self.__up_side = False
        self.__down_side = False

    def get_owner(self):
        return self.__owner

    def add_owner(self, owner):
        self.__owner = owner

    def has_line_on_side(self, side):
        if side == Box.LEFT:
            return self.__left_side
        elif side == Box.UP:
            return self.__up_side
        elif side == Box.RIGHT:
            return self.__right_side
        else:
            return self.__down_side

    def add_line(self, side):
        if side == Box.LEFT and not self.__left_side:
            self.__left_side = True
        elif side == Box.UP and not self.__up_side:
            self.__up_side = True
        elif side == Box.RIGHT and not self.__right_side:
            self.__right_side = True
        elif side == Box.DOWN and not self.__down_side:
            self.__down_side = True
        else:
            return False
        return True

    def four_lines_placed(self):
        return self.__left_side and self.__up_side and self.__right_side and self.__down_side
