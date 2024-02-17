import pytest
from src.mars_rover import MarsRover, FacingDirection
 
MOVE_FORWARD_TEST_LIST = [
    (FacingDirection.NORTH, [0, 1]),
    (FacingDirection.SOUTH, [0, -1]),
    (FacingDirection.EAST, [1, 0]),
    (FacingDirection.WEST, [-1, 0])
]


@pytest.mark.parametrize("direction, expected", MOVE_FORWARD_TEST_LIST)
def test_move_forward(direction: FacingDirection, expected: list[int]):
    rover = MarsRover(x=0, y=0, direction=direction)
    rover.move_forward()
    assert rover.location() == expected


MOVE_BACKWARDS_TEST_LIST = [
    (FacingDirection.NORTH, [0, -1]),
    (FacingDirection.SOUTH, [0, 1]),
    (FacingDirection.EAST, [-1, 0]),
    (FacingDirection.WEST, [1, 0])
]


@pytest.mark.parametrize("direction, expected", MOVE_BACKWARDS_TEST_LIST)
def test_move_backwards(direction: FacingDirection, expected: list[int]):
    rover = MarsRover(x=0, y=0, direction=direction)
    rover.move_backwards()
    assert rover.location() == expected


TURN_LEFT_TEST_LIST = [
    (FacingDirection.NORTH, FacingDirection.WEST),
    (FacingDirection.WEST, FacingDirection.SOUTH),
    (FacingDirection.SOUTH, FacingDirection.EAST),
    (FacingDirection.EAST, FacingDirection.NORTH)
]


@pytest.mark.parametrize("direction, expected", TURN_LEFT_TEST_LIST)
def test_turn_left(direction: FacingDirection, expected: str):
    rover = MarsRover(x=0, y=0, direction=direction)
    rover.turn_left()
    assert rover.direction == expected


TURN_RIGHT_TEST_LIST = [
    (FacingDirection.NORTH, FacingDirection.EAST),
    (FacingDirection.WEST, FacingDirection.NORTH),
    (FacingDirection.SOUTH, FacingDirection.WEST),
    (FacingDirection.EAST, FacingDirection.SOUTH)
]


@pytest.mark.parametrize("direction, expected", TURN_RIGHT_TEST_LIST)
def test_turn_right(direction: FacingDirection, expected: str):
    rover = MarsRover(x=0, y=0, direction=direction)
    rover.turn_right()
    assert rover.direction == expected


def test_instructions():
    rover = MarsRover(x=0, y=0, direction=FacingDirection.NORTH)
    rover.instructions("FFLCFRB")
    assert rover.location() == [-1, 1] and rover.direction == FacingDirection.NORTH
