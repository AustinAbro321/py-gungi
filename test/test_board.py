from approvaltests import verify

from board import starting_board, Board, translate_square_to_tuple
from color import Color
from hand import starting_hand
from move import MoveInfo, move
from square import *
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
    board.content[0][0] = PieceStack([Piece(PieceType.MAJOR_GENERAL, Color.WHITE)])
    verify(move(board, MoveInfo(Square(A1), Square(B1))))

def test_move_approvals_two_on_stack():
    board = Board(starting_board())
    board.content[0][0] = PieceStack([Piece(PieceType.MAJOR_GENERAL, Color.WHITE),
                                      Piece(PieceType.MAJOR_GENERAL, Color.WHITE)])
    make_move(board, MoveInfo(Square(A1), Square(B1)))

def make_move(board: Board, move_info):
    verify(move(board, move_info))

def test_get_piece_stack_a1():
    get_piece_stack_given_square(0, 0, A1)

def test_get_piece_stack_b7():
    get_piece_stack_given_square(6,1,B7)

def test_get_piece_stack_f9():
    get_piece_stack_given_square(8,8,F9)

def test_get_piece_stack_d8():
    get_piece_stack_given_square(7,3,D8)

def get_piece_stack_given_square(row: int, col: int,square: Square):
    e_row,e_col = translate_square_to_tuple(square)
    assert e_row == row
    assert e_col == col
