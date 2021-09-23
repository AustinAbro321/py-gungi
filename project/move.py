import typing
from dataclasses import dataclass
import copy
from board import Board


@dataclass
class Square:
    row: int
    col: int

@dataclass
class MoveInfo:
    point_a: Square
    point_b: Square

def translate_move() -> MoveInfo:
    return MoveInfo(Square(0,0),Square(0,1))

def move(board : Board,move_info: MoveInfo) -> Board:
    new_board = board
    point_a = move_info.point_a
    point_b = move_info.point_b
    new_board.content[point_b.row][point_b.col] = copy.deepcopy(board.content[point_a.row][point_a.col])
    board.content[point_a.row][point_a.col].pop()
    new_board.content[point_a.row][point_a.col] = board.content[point_a.row][point_a.col]
    return new_board
