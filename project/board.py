from .piece import PieceStack
from .square import Square, A1, B7


def starting_board() -> 'list[list[PieceStack]]':
    return [
        [PieceStack([]),PieceStack([]),PieceStack([]),PieceStack([]),
        PieceStack([]),PieceStack([]),PieceStack([]),PieceStack([]),PieceStack([])],
        [PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]),
        PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([])],
        [PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]),
        PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([])],
        [PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]),
        PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([])],
        [PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]),
        PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([])],
        [PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]),
        PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([])],
        [PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]),
        PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([])],
        [PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]),
        PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([])],
        [PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]),
        PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([]), PieceStack([])]]


class Board:
    def __init__(self, content: 'list[list[PieceStack]]'):
        self.content = content

    def __repr__(self):
        name = ""
        for line in self.content:
            name += "["
            name += ", ".join([pieceStack.__repr__() for pieceStack in line])
            name += "]"
            name += "\n"
        return name

    def get_piece_at(self, square: Square):
        row,col = translate_square_to_tuple(square)
        return self.content[row][col]

def translate_square_to_tuple(square: Square):
    row = (square // 9)
    col = (square % 9)
    return row,col
