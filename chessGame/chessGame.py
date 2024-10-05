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
    """Verifica si un movimiento es valido"""
    sx, sy = start
    ex, ey = end
    piece = board[sx][sy]

    #verificar que la pieza sea del oponente
    if (player=="white" and piece.islower()) or (player=="black" and piece.isupper()):
        return False

    #verificar que la casilla de destino no sea una pieza del oponente
    target_piece = board[ex][ey]
    if (player=="white" and target_piece.isupper()) or (player=="black" and target_piece.islower()):
        return False
    
    #verificar que la casilla de destino sea vacia
    if target_piece != " ":
        return False
    
    #definir el desplazamiento
    dx,dy =abs(ex-sx),abs(ey-sy)

    if piece.lower() == "p":
        direction = 1 if piece.isupper() else -1 
        if dy == 0 and board[ex][ey] == " ":
            if dx == 1 or (dx == 2 and ((sx == 6 and piece.isupper()) or (sx == 1 and piece.islower()))):
                return True
        elif dx == 1 and dy == 1 and board[ex][ey] != " ":
            return True
        
    elif piece.lower() == "r":
        if dx == 0 or dy == 0:
            return is_clear_path(start, end)
    
    elif piece.lower() == "n":
        if (dx,dy) in [(1,2),(2,1)]:
            return True
    
    elif piece.lower() == "b":
        if dx == dy:
            return is_clear_path(start, end)
    
    elif piece.lower() == "q":
        if dx == dy or dx == 0 or dy == 0:
            return is_clear_path(start, end)

    elif piece.lower() == "k":
        if max(dx,dy) == 1:
            return True
        
    return False

def is_clear_path(start, end):
    """Verifica si el camino entre dos puntos es vacio."""
    sx, sy = start
    ex, ey = end
    
    dx = 1 if ex > sx else -1 if ex < sx else 0
    dy = 1 if ey > sy else -1 if ey < sy else 0

    x, y = sx +dx, sy + dy
    while (x, y) != (ex, ey):
        if board[x][y] != " ":
            return False
        x += dx
        y += dy
    return True

def is_valid_castling(player, move):
    """Verifica si el enroque es posible."""
    if player == "white":
        row = 7
        if move == "o-o":  
            if board[row][4] == "K" and board[row][7] == "R":
                if board[row][5] == " " and board[row][6] == " ":
                    return True
        elif move == "o-o-o": 
            if board[row][4] == "K" and board[row][0] == "R":
                if board[row][1] == " " and board[row][2] == " " and board[row][3] == " ":
                    return True
    else:
        row = 0
        if move == "o-o":  
            if board[row][4] == "k" and board[row][7] == "r":
                if board[row][5] == " " and board[row][6] == " ":
                    return True
        elif move == "o-o-o": 
            if board[row][4] == "k" and board[row][0] == "r":
                if board[row][1] == " " and board[row][2] == " " and board[row][3] == " ":
                    return True
    return False




def move_piece(start, end, move=None):
    """Mueve una pieza de un lugar a otro."""

    if move == "o-o":
        if board[7][4] == "K":
            board[7][6] = "K"
            board[7][5] = "R"
            board[7][4] = " "
            board[7][7] = " "
        else:
            board[0][6] = "k"
            board[0][5] = "r"
            board[0][4] = " "
            board[0][7] = " "
    elif move == "o-o-o":
        if board[7][4] == "K":
            board[7][2] = "K"
            board[7][3] = "R"
            board[7][4] = " "
            board[7][0] = " "
        else:
            board[0][2] = "k"
            board[0][3] = "r"
            board[0][4] = " "
            board[0][0] = " "
    else:
        sx, sy = start
        ex, ey = end
        board[ex][ey] = board[sx][sy]
        board[sx][sy] = " "

def parse_input(move):
    """Convierte la entrada de texto en coordenadas del tablero."""
    if move in ["o-o", "o-o-o"]:
        return None, None, move
    try:
        start, end = move.split()
        sx, sy = 8 - int(start[1]), column_map[start[0]]
        ex, ey = 8 - int(end[1]), column_map[end[0]]
        return (sx, sy), (ex, ey), None
    except (ValueError, IndexError, KeyError):
        return None, None, None

def main():
    """Funcion principal para ejecutar el juego."""
    player = "white"
    while True:
        print_board()
        print(f"Turno de {player}. Ejemplo de movimiento: e2 e4, o-o para enrocar en corto, o-o-o para enrocar en largo.")
        move = input("Ingresa tu movimiento: ")

        if move.upper() == "FIN":
            print("Juego terminado.")
            break

        start, end, castling = parse_input(move)

        if castling:
            if is_valid_castling(player, castling):
                move_piece(None, None, castling)
                player = "black" if player == "white" else "white"  # Cambiar turno
            else:
                print("Enroque no valido. Intenta de nuevo.")

        elif start is None or end is None:
            print("Movimiento invalido. Intenta de nuevo.")
            continue

        elif is_valid_move(start, end, player):
            move_piece(start, end)
            player = "black" if player == "white" else "white"  # Cambiar turno
        else:
            print("Movimiento no valido. Intenta de nuevo.")

main()
