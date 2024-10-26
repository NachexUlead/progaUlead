from piece import Piece

class Pawn(Piece):
    def move(self, destination, board):
        initialRow, initialCol = self.position
        destRow, destCol = destination
        direction = -1 if self.color == "white" else 1

        if initialCol == destCol:
            if destRow == initialRow + direction:
                return True
            startingRow = 6 if self.color == "white" else 1
            if initialRow == startingRow and destRow == initialRow + 2 * direction:
                return True
        if abs(destCol - initialCol) == 1 and destRow == initialRow + direction:
            return True

        return False
