from enum import Enum


class FacingDirection(Enum):
    NORTH = 1
    EAST = 2
    WEST = 3
    SOUTH = 4


class MarsRover:
    def __init__(self, x: int, y: int, direction: FacingDirection) -> None:
        self.x = x
        self.y = y
        self.direction = direction

    def instructions(self, inst: str):
        insts = [*inst]
        for i in insts:
            if i == "F":
                self.move_forward()
            elif i == "B":
                self.move_backwards()
            elif i == "R":
                self.turn_right()
            elif i == "L":
                self.turn_left()
            else:
                pass

    def location(self):
        return [self.x, self.y]

    def move(self, step: int) -> None:
        if self.direction == FacingDirection.NORTH:
            self.y += step
        elif self.direction == FacingDirection.SOUTH:
            self.y -= step
        elif self.direction == FacingDirection.EAST:
            self.x += step
        elif self.direction == FacingDirection.WEST:
            self.x -= step

    def move_forward(self):
        self.move(1)

    def move_backwards(self):
        self.move(-1)

    def turn_left(self):
        if self.direction == FacingDirection.NORTH:
            self.direction = FacingDirection.WEST
        elif self.direction == FacingDirection.WEST:
            self.direction = FacingDirection.SOUTH
        elif self.direction == FacingDirection.SOUTH:
            self.direction = FacingDirection.EAST
        elif self.direction == FacingDirection.EAST:
            self.direction = FacingDirection.NORTH

    def turn_right(self):
        if self.direction == FacingDirection.NORTH:
            self.direction = FacingDirection.EAST
        elif self.direction == FacingDirection.WEST:
            self.direction = FacingDirection.NORTH
        elif self.direction == FacingDirection.SOUTH:
            self.direction = FacingDirection.WEST
        elif self.direction == FacingDirection.EAST:
            self.direction = FacingDirection.SOUTH
