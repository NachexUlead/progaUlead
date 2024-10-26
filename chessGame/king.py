from piece import Piece

class King(Piece):
    def move(self, destination):
        initialRow, initialCol = self.position
        destRow, destCol = destination
        dx, dy = abs(destRow - initialRow), abs(destCol - initialCol)
        return max(dx, dy) == 1
