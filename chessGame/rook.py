from piece import Piece
from utils import isClearPath

class Rook(Piece):
    def move(self, destination, board):
        startRow, startCol = self.position
        endRow, endCol = destination
        if startRow == endRow or startCol == endCol:
            return isClearPath(self.position, destination, board)
        return False
