from piece import Piece

class Rook(Piece):
    def move(self, destination):
        initialRow, initialCol = self.position
        destRow, destCol = destination
        return initialRow == destRow or initialCol == destCol
