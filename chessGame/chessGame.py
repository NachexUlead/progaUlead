# Inicializar el tablero de ajedrez vacio
board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]

# Mapeo de columnas de letras a indices
column_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

def print_board():
    """Imprime el tablero de ajedrez en consola."""
    print("  a b c d e f g h")
    for i, row in enumerate(board):
        print(8 - i, end=" ")
        print(" ".join(row))
    print()

def is_valid_move(start, end, player):
    """Verifica si un movimiento es valido (basico sin reglas complejas)."""
    sx, sy = start
    ex, ey = end
    piece = board[sx][sy]

    #verificar que la pieza sea del oponente
    if (player=="white" and piece.islower()) or (player=="black" and piece.isupper()):
        return False
    
    target_piece = board[ex][ey]

    

    # if piece == " ":
    #     return False  # No hay pieza para mover

    # if (player == "white" and piece.islower()) or (player == "black" and piece.isupper()):
    #     return False  # No se puede mover la pieza del oponente

    # target_piece = board[ex][ey]
    # if (player == "white" and target_piece.isupper()) or (player == "black" and target_piece.islower()):
    #     return False  # No se puede capturar la propia pieza


    return True

def move_piece(start, end):
    """Mueve una pieza de un lugar a otro."""
    sx, sy = start
    ex, ey = end
    board[ex][ey] = board[sx][sy]
    board[sx][sy] = " "

def parse_input(move):
    """Convierte la entrada de texto en coordenadas del tablero."""
    try:
        start, end = move.split()
        sx, sy = 8 - int(start[1]), column_map[start[0]]
        ex, ey = 8 - int(end[1]), column_map[end[0]]
        return (sx, sy), (ex, ey)
    except (ValueError, IndexError, KeyError):
        return None, None

def main():
    """Funcion principal para ejecutar el juego."""
    player = "white"
    while True:
        print_board()
        print(f"Turno de {player}. Ejemplo de movimiento: e2 e4")
        move = input("Ingresa tu movimiento: ")

        if move.lower() == "salir":
            print("Juego terminado.")
            break

        start, end = parse_input(move)

        if start is None or end is None:
            print("Movimiento invalido. Intenta de nuevo.")
            continue

        if is_valid_move(start, end, player):
            move_piece(start, end)
            player = "black" if player == "white" else "white"  # Cambiar turno
        else:
            print("Movimiento no valido. Intenta de nuevo.")

main()
