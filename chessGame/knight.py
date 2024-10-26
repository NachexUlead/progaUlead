from piece import Piece

class Knight(Piece):
    def move(self, destination):
        initialRow, initialCol = self.position
        destRow, destCol = destination
        dx, dy = abs(destRow - initialRow), abs(destCol - initialCol)
        return (dx, dy) in [(1, 2), (2, 1)]
