from approvaltests import verify

from board import starting_board, Board
from color import Color
from hand import starting_hand
from move import MoveInfo, Square, move
from piece import Piece, PieceType, PieceStack


def test_board_init():
    assert True


def test_color():
    assert Color.WHITE == Color.WHITE


def test_starting_hand():
    assert starting_hand(Color.WHITE) == [Piece(PieceType.MAJOR_GENERAL, Color.WHITE),
                                          Piece(PieceType.MAJOR_GENERAL, Color.WHITE),
                                          Piece(PieceType.MAJOR_GENERAL, Color.WHITE),
                                          Piece(PieceType.MAJOR_GENERAL, Color.WHITE)]

def test_move_approvals():
    board = Board(starting_board())
    piece_stack = PieceStack([Piece(PieceType.MAJOR_GENERAL, Color.WHITE)])
    board.content[0][0] = piece_stack
    move_info = MoveInfo(Square(0,0),Square(0,1))
    verify(move(board,move_info))