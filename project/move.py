from dataclasses import dataclass
from .board import Board
from .square import *


@dataclass
class MoveInfo:
    point_a: Square
    point_b: Square

def translate_move() -> MoveInfo:
    return MoveInfo(Square(A1),Square(A2))

def move(board : Board,move_info: MoveInfo) -> Board:
    new_board = board
    new_board.get_piece_at(move_info.point_b) \
        .add(board.get_piece_at(move_info.point_a).pop())
    return new_board
