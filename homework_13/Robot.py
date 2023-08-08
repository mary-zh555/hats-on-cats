# 4. Create a Robot class with the following attributes: orientation (left, right, up, down), position_x, position_y.
# The Robot class should have the following methods: move, turn, and display_position.
# The move method should take a number of steps and move the robot in the direction it is currently facing.
# The turn method should take a direction (left or right) and turn the robot in that direction.
# The display_position method should print the current position of the robot.


from Board import Board


class Robot:
    ORIENTATIONS: list = ["down", "right", "up", "left"]
    DIRECTIONS: list = ["left", "right"]

    def __init__(
        self, orientation: str, position_x: int, position_y: int, board: Board
    ):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y
        self.board = board

    def move(self, steps: int):
        # check if able to move/check if in the edge of the board:
        able_to_move = True
        if (
            (self.position_x == 1 and self.orientation == "left")
            or (self.position_y == 1 and self.orientation == "up")
            or (self.position_x == self.board.max_x and self.orientation == "right")
            or (self.position_y == self.board.max_y and self.orientation == "down")
        ):
            able_to_move = False

        if able_to_move:
            if self.orientation == "down":
                self.position_y += steps

            if self.orientation == "right":
                self.position_x += steps

            if self.orientation == "up":
                self.position_y -= steps

            if self.orientation == "left":
                self.position_x -= steps

            print(f"Moving {steps} steps further.")
            if (
                (self.position_x == 1 and self.orientation == "left")
                or (self.position_y == 1 and self.orientation == "up")
                or (self.position_x == self.board.max_x and self.orientation == "right")
                or (self.position_y == self.board.max_y and self.orientation == "down")
            ):
                print("❌ Unable to move further, facing the wall!")
        else:
            print("❌ The robot is facing the wall, please turn it to move!")

    def turn(self, direction: str):
        current_index = Robot.ORIENTATIONS.index(self.orientation)
        multiplied_list = Robot.ORIENTATIONS * 2
        if direction == "left":
            self.orientation = multiplied_list[current_index + 1]
        if direction == "right":
            self.orientation = multiplied_list[current_index - 1]
        print(f"Turning {direction}")

    def display_position(self):
        return f"🌐 On the board {self.board.max_x} x {self.board.max_y}: Robot is facing {self.orientation}, located on the x = {self.position_x}, y = {self.position_y}."
