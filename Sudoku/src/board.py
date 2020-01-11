# from data import easy
from Sudoku.Sudoku.src.data import easy

class Board:
    
    def __init__(self, grid):
        self.grid = grid

    def display_board(self):
        print(self.grid)


def main():
    b = Board(easy)
    b.display_board()

if __name__ == '__main__':
    main()