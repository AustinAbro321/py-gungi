from color import Color
from project.hand import Hand, starting_hand
from project.piece import Piece, PieceType


def test_board_init():
    assert True


def test_color():
    print(Color.WHITE)
    print(Color.WHITE)
    print(Color.WHITE)
    print(Color.WHITE)
    assert Color.WHITE == Color.WHITE


def test_starting_hand():
    assert starting_hand(Color.WHITE) == [Piece(PieceType.MAJOR_GENERAL, Color.White),
                                          Piece(PieceType.MAJOR_GENERAL, Color.White),
                                          Piece(PieceType.MAJOR_GENERAL, Color.White),
                                          Piece(PieceType.MAJOR_GENERAL, Color.White)]
