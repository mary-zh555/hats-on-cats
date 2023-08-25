# The bard class to make the location non-infinite
class Board:
    def __init__(self, max_x: int, max_y: int):
        # start point for x ang y = 1 by default
        self.max_x = max_x
        self.max_y = max_y
