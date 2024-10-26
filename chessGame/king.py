from piece import Piece

class King(Piece):
    def move(self, destination, board):
        startRow, startCol = self.position
        endRow, endCol = destination
        return max(abs(startRow - endRow), abs(startCol - endCol)) == 1
