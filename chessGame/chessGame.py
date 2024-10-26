from pawn import Pawn
from queen import Queen
from knight import Knight
from rook import Rook
from king import King
from bishop import Bishop

defaultBoard = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

columnMap = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

def printBoard(board):
    """Prints the chessboard to the console."""
    print("  a b c d e f g h")
    for i, row in enumerate(board):
        print(8 - i, end=" ")
        print(" ".join(row))
    print()

def parsePosition(position):
    """Converts a position in algebraic notation (e.g., 'e2') to board coordinates."""
    column = columnMap[position[0]]
    row = 8 - int(position[1])
    return (row, column)

def initializePieces():
    """Initialize both white and black pieces with their starting positions."""
    pieces = [
        Pawn("white", (6, 0)), Pawn("white", (6, 1)), Pawn("white", (6, 2)), Pawn("white", (6, 3)),
        Pawn("white", (6, 4)), Pawn("white", (6, 5)), Pawn("white", (6, 6)), Pawn("white", (6, 7)),
        Rook("white", (7, 0)), Knight("white", (7, 1)), Bishop("white", (7, 2)), Queen("white", (7, 3)),
        King("white", (7, 4)), Bishop("white", (7, 5)), Knight("white", (7, 6)), Rook("white", (7, 7)),
        
        Pawn("black", (1, 0)), Pawn("black", (1, 1)), Pawn("black", (1, 2)), Pawn("black", (1, 3)),
        Pawn("black", (1, 4)), Pawn("black", (1, 5)), Pawn("black", (1, 6)), Pawn("black", (1, 7)),
        Rook("black", (0, 0)), Knight("black", (0, 1)), Bishop("black", (0, 2)), Queen("black", (0, 3)),
        King("black", (0, 4)), Bishop("black", (0, 5)), Knight("black", (0, 6)), Rook("black", (0, 7)),
    ]
    return pieces

def findPieceAtPosition(pieces, position):
    """Finds a piece in the pieces list based on a given position."""
    for piece in pieces:
        if piece.position == position:
            return piece
    return None

def movePiece(piece, destination, board):
    if piece.move(destination, board): 
        startRow, startCol = piece.position
        endRow, endCol = destination
        board[startRow][startCol] = " "
        board[endRow][endCol] = piece.__class__.__name__[0].upper() if piece.color == "white" else piece.__class__.__name__[0].lower()
        
        piece.position = destination
        print(f"Move of {piece} to {destination} is valid.")
    else:
        print(f"Move of {piece} to {destination} is not valid.")

def main():
    print("Welcome to the chess game")
    board = [row[:] for row in defaultBoard]
    pieces = initializePieces()
    printBoard(board)

    currentPlayer = "white"
    
    while True:
        print(f"{currentPlayer.capitalize()}'s turn")
        move = input("Enter your move (e.g., 'e2 e4') or 'exit' to quit: ")
        
        if move.lower() == "exit":
            print("Game ended.")
            break

        try:
            start, end = move.split()
            startPos = parsePosition(start)
            endPos = parsePosition(end)

            piece = findPieceAtPosition(pieces, startPos)
            if piece:
                if piece.color == currentPlayer:
                    movePiece(piece, endPos, board)
                    currentPlayer = "black" if currentPlayer == "white" else "white"
                else:
                    print(f"Invalid move: It's {currentPlayer}'s turn.")
            else:
                print("No piece at the specified start position.")
        except ValueError:
            print("Invalid input format. Please enter moves in the format 'e2 e4'.")
        
        printBoard(board)

if __name__ == "__main__":
    main()
