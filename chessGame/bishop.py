from piece import Piece
from utils import isClearPath

class Bishop(Piece):
    def move(self, destination, board):
        startRow, startCol = self.position
        endRow, endCol = destination
        if abs(startRow - endRow) == abs(startCol - endCol):
            return isClearPath(self.position, destination, board)
        return False
