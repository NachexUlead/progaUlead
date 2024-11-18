def create_board(size):
    """Creates an empty board of the given size."""
    return [[" " for _ in range(size)] for _ in range(size)]


def print_board(board):
    """Prints the board to the console."""
    for row in board:
        print(" ".join(row))


def place_piece(board, x, y, piece):
    """Places a piece at a specific position on the board."""
    if board[x][y] == " ":
        board[x][y] = piece
        return True
    return False


def move_piece(board, x1, y1, x2, y2):
    """Moves a piece from one position to another if the move is valid."""
    if board[x1][y1] != " " and board[x2][y2] == " ":
        # Check if the move is to an adjacent cell
        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
            board[x2][y2] = board[x1][y1]
            board[x1][y1] = " "
            return True
        else:
            print("You can only move to an adjacent cell. Try again.")
    else:
        print("Invalid move. Either the starting position is empty or the destination is occupied.")
    return False


def get_coordinates(size):
    """Asks the user for valid coordinates within the board boundaries."""
    while True:
        try:
            user_input = input("Enter coordinates (x y): ").strip()
            if not user_input:  # Handle empty input
                print("Input cannot be empty. Please enter valid coordinates.")
                continue
            x, y = map(int, user_input.split())
            if 0 <= x < size and 0 <= y < size:
                return x, y
            else:
                print(f"Coordinates must be between 0 and {size - 1}. Try again.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
