from data import easy
from utils import check_col, check_row, check_local_square

def pretty_row(arr):
    """
    Splits rows into groups of threes suitable for 9x9 Sudoku board
    """
    assert arr.shape == (9,), 'not valid Sudoku row'
    row = []
    for i, v in enumerate(arr):
        if i == 3 or i == 6:
            print('| ', end='')
        print(f'{v} ', end='')
    return row

class Board:
    """
    Very generic Board class to hold unsolved grid
    """
    
    def __init__(self, grid):
        self.grid = grid
        """
        Create data structure grid[i][j] = [1,0,0,0,1,0,0,1,1]
        which represents (1,5,8,9) are the only legal moves
        """

    def find_best_empty_cell(self):
        """
        Finds the (row, col) of a cell that has the lowest number of legal moves
        Returns None if grid is copmlete
        """
        pass

    def display_board(self):
        """
        Displays 9x9 Sudoku board in recognisable format
        """
        assert self.grid.shape == (9,9), 'Not standard Sudoku grid shape'
        for i, row in enumerate(self.grid):
            if i == 3 or i == 6:
                print('---------------------')
            pretty_row(row)
            print('\r')

    def is_legal_move(self, num, i, j):
        """
        Checks to see if num is already present in the row / col / local square \
            defined by (i, j) position of input
        """
        args = (self.grid, num, i, j)
        return (not check_row(*args)) and (not check_col(*args)) and (not check_local_square(*args))


def main():
    b = Board(easy)
    b.display_board()

if __name__ == '__main__':
    main()