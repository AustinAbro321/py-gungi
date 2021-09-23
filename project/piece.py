from dataclasses import dataclass
from enum import Enum
from color import Color


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


class PieceStack:
    def __init__(self,pieces: list[Piece] = []):
        self.pieces = pieces

    def pop(self) -> Piece:
        return self.pieces.pop()

    # def __str__(self) -> str:
    #     name = ""
    #     for piece in self.pieces:
    #         name += str(piece.piece_type.value)
    #     return name

    def __repr__(self) -> str:
        name = "piece"
        for piece in self.pieces:
            name += str(piece.piece_type.value)
        return name