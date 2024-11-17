class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        # Initialize the grid with spaces (as strings)
        self.board = [[" " for _ in range(columns)] for _ in range(rows)]

    def display_board(self):
        for row in self.board:
            print(" | ".join(row))  # Join each row's elements with "|"
            print("-" * (self.columns * 3 - 1))  # Print a separator line
