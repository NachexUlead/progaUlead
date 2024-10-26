from piece import Piece

class Pawn(Piece):
    def move(self, destination):
        initialRow, initialCol = self.position
        destRow, destCol = destination
        direction = -1 if self.color == "white" else 1  # White moves up, black moves down

        # Move forward by one square
        if initialCol == destCol:
            # Allow single-step forward move
            if destRow == initialRow + direction:
                return True
            # Allow two-square initial move if on the starting row
            startingRow = 6 if self.color == "white" else 1
            if initialRow == startingRow and destRow == initialRow + 2 * direction:
                return True

        # Diagonal capture move
        if abs(destCol - initialCol) == 1 and destRow == initialRow + direction:
            return True

        return False
