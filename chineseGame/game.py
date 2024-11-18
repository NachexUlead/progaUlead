from functions import create_board, print_board, place_piece, move_piece, get_coordinates

class Player:
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece

    def make_move(self, board):
        print(f"{self.name}'s turn ({self.piece})")
        while True:
            start = get_coordinates(len(board.board))
            end = get_coordinates(len(board.board))
            if move_piece(board.board, start[0], start[1], end[0], end[1]):
                print(f"{self.name} moved from {start} to {end}")
                break
            else:
                print("Invalid move. Try again.")


class ChineseCheckersGame:
    def __init__(self):
        self.board = Board()
        self.players = []

    def setup_game(self):
        num_players = int(input("Enter the number of players (2-6): "))
        pieces = ["A", "B", "C", "D", "E", "F"][:num_players]
        for i in range(num_players):
            name = input(f"Enter the name for Player {i + 1}: ")
            self.players.append(Player(name, pieces[i]))

        for i, player in enumerate(self.players):
            start_row = i * 2
            for j in range(i + 1):
                place_piece(self.board.board, start_row, j, player.piece)

    def play_game(self):
        current_player_index = 0
        while True:
            print_board(self.board.board)
            player = self.players[current_player_index]
            player.make_move(self.board)
            current_player_index = (current_player_index + 1) % len(self.players)


class Board:
    def __init__(self, size=17):
        self.size = size
        self.board = create_board(size)


if __name__ == "__main__":
    game = ChineseCheckersGame()
    game.setup_game()
    game.play_game()
