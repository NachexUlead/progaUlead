from piece import Piece

class Queen(Piece):
    def move(self, destination):
        initialRow, initialCol = self.position
        destRow, destCol = destination
        dx, dy = abs(destRow - initialRow), abs(destCol - initialCol)
        
        return dx == dy or initialRow == destRow or initialCol == destCol
