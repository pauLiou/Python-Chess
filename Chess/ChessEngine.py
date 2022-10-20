'''
This class is responsible for storing all the information about the current state of the chess game. It will also be responsible
for determining the valid moves at the current state. It will also keep a move log.
'''

class GameState():
    def __init__(self):
        # board is an 8x8 2d list, each element of the list has 2 characters.
        # first character represents colour, second character represents the piece type.
        # "--" represents an empty space.
        self.board = [ # probably worth redoing this with numpy in the future
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []
