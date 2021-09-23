from piece import PieceStack


def starting_board() -> list[list[PieceStack]]:
    return [
        [PieceStack(),PieceStack(),PieceStack(),PieceStack(),
        PieceStack(),PieceStack(),PieceStack(),PieceStack(),PieceStack()],
        [PieceStack(), PieceStack(), PieceStack(), PieceStack(),
        PieceStack(), PieceStack(), PieceStack(), PieceStack(), PieceStack()],
        [PieceStack(), PieceStack(), PieceStack(), PieceStack(),
        PieceStack(), PieceStack(), PieceStack(), PieceStack(), PieceStack()],
        [PieceStack(), PieceStack(), PieceStack(), PieceStack(),
        PieceStack(), PieceStack(), PieceStack(), PieceStack(), PieceStack()],
        [PieceStack(), PieceStack(), PieceStack(), PieceStack(),
        PieceStack(), PieceStack(), PieceStack(), PieceStack(), PieceStack()],
        [PieceStack(), PieceStack(), PieceStack(), PieceStack(),
        PieceStack(), PieceStack(), PieceStack(), PieceStack(), PieceStack()],
        [PieceStack(), PieceStack(), PieceStack(), PieceStack(),
        PieceStack(), PieceStack(), PieceStack(), PieceStack(), PieceStack()],
        [PieceStack(), PieceStack(), PieceStack(), PieceStack(),
        PieceStack(), PieceStack(), PieceStack(), PieceStack(), PieceStack()],
        [PieceStack(), PieceStack(), PieceStack(), PieceStack(),
        PieceStack(), PieceStack(), PieceStack(), PieceStack(), PieceStack()]]


class Board:
    def __init__(self, content: list[list[PieceStack]]):
        self.content = content

    def __repr__(self):
        name = ""
        for line in self.content:
            name += "["
            for pieceStack in line:
                name += pieceStack.__repr__() + ","
            name += "]"
            name += "\n"
        return name
