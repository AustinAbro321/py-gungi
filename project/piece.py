from dataclasses import dataclass
from enum import Enum
from .color import Color
from .square import Square


class PieceType(Enum):
    MAJOR_GENERAL = 1
    LIEUTENANT_GENERAL = 2
    GENERAL = 3
    ARCHER = 4
    KNIGHT = 5
    MUSKETEER = 6
    CAPTAIN = 7
    SAMURAI = 8
    FORTRESS = 9
    CANNON = 10
    SPY = 11
    PAWN = 12
    KING = 13


@dataclass
class Piece:
    piece_type: PieceType
    color: Color

class MajorGeneral:
    def available_movements(self,place_in_stack: int) -> 'list[Square]':
        pass

class PieceStack:
    def __init__(self,pieces = []):
        self.pieces = pieces

    def pop(self) -> Piece:
        return self.pieces.pop()

    def add(self,piece:Piece):
        self.pieces.append(piece)

    def __repr__(self) -> str:
        return "[" + ", ".join([piece.piece_type.name for piece in self.pieces]) + "]"
