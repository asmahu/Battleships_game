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

         # adds "*" if selected coordinates hits a target
        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="CPU"):
        if len(self.ships) >= self.number_ships:
            print("Error: you cannot add any more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "#"

    def random_point(size):

        """
        Helper function to return a random integer between o and size
        """
        return randint(0, size - 1)


    def validate_coordinates(x, y, board):

    """
    Function to validate coordinate inputs from users
    """

    try:
        x, y = int(x), int(y)
        board.board[x][y] in board.board

    except IndexError:
        print("Invalid input: row and column\
must be an integer between 0 - {board.size - 1} \n")
        return False

    except ValueError:
        print("Invalid input: sorry, only integer numbers are allowed.\n")
        return False

    finally:
        if (x, y) in board.guesses:
            print("Boat does not fit. please input different coordinates!!!\n")
            return False
    return True
