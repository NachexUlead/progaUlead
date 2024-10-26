def isClearPath(start, end, board):
    """Checks if the path between two squares is clear for sliding pieces to move."""
    startRow, startCol = start
    endRow, endCol = end

    # Determine step for row and column
    stepRow = 1 if endRow > startRow else -1 if endRow < startRow else 0
    stepCol = 1 if endCol > startCol else -1 if endCol < startCol else 0

    # Check each square along the path
    currentRow, currentCol = startRow + stepRow, startCol + stepCol
    while (currentRow, currentCol) != (endRow, endCol):
        if board[currentRow][currentCol] != " ":
            return False  # Path is blocked
        currentRow += stepRow
        currentCol += stepCol

    return True  # Path is clear
