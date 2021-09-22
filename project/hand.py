from piece import Piece, PieceType
from color import Color


def starting_hand(player: Color):
    hand = []
    hand.extend([Piece(PieceType.MAJOR_GENERAL, player)] * 4)
    hand.extend([Piece(PieceType.LIEUTENANT_GENERAL, player)] * 4)
    return hand
    # Piece(PieceType.LIEUTENANT_GENERAL, player), Piece(PieceType.LIEUTENANT_GENERAL, player),
    # Piece(PieceType.LIEUTENANT_GENERAL, player), Piece(PieceType.LIEUTENANT_GENERAL, player),
    # Piece(PieceType.GENERAL, player), Piece(PieceType.GENERAL, player), Piece(PieceType.GENERAL, player),
    # Piece(PieceType.GENERAL, player), Piece(PieceType.GENERAL, player), Piece(PieceType.GENERAL, player),
    # Piece(PieceType.Archer, player), Piece(PieceType.Archer, player),
    # Piece(PieceType.Knight, player), ]


class Hand:
    def __init__(self, player: Color):
        self.player = Color.WHITE
        self.hand = starting_hand(player)
        print(starting_hand(player))
