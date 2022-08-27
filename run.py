from random import randint
import sys

scores = {'CPU': 0, 'player': 0}


# Board class adopted and modified from the CI's battleship tutorial
class Board:

    """
    Main board class. to set board size, the number of ships,
     the player's name and the player board or CPU
     contains methods to add ships, guesses and to print the board
    """

    def __init__(self, size, number_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.number_ships = number_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        # prints board
        for row in self.board:
            print("  ".join(row))

    def guess(self, x, y):
        # adds "x" at the selected coordinates
        self.board[x][y] = "x"
