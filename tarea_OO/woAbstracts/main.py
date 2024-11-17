from board import Board
from trasnformer_xml import TransformerXML

board = Board(8, 8)
board.display_board()


class Example:
    def __init__(self):
        self.__private = "only visible in XML"
        self.public = "visible in XML and Python"

obj = Example()
transformer = TransformerXML()
xml = transformer.serialize(obj)


print(xml)