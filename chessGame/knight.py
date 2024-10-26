from piece import Piece

class Knight(Piece):
    def move(self, destination, board):
        startRow, startCol = self.position
        endRow, endCol = destination
        return (abs(startRow - endRow), abs(startCol - endCol)) in [(2, 1), (1, 2)]
