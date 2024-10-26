class Piece:
    def __init__(self, color, position):
        self.color = color  # "white" or "black"
        self.position = position  # Position in the format (row, column)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.color == other.color and self.position == other.position

    def __str__(self):
        return f"{self.__class__.__name__} {self.color} at {self.position}"