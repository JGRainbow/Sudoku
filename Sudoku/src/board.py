import numpy as np

from data import easy, intermediate
from utils import (check_col, 
                    check_row, 
                    check_local_square,
                    find_affected_cells,
                    check_position_is_legal)

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
        self.size = grid.shape[0]
        """
        Create data structure grid_possibilities[i][j] = [1,0,0,0,1,0,0,1,1]
        which represents that (1,5,8,9) are the only legal moves
        N.B. We must subtract one from the index for python lists
        """
        self.grid_possibilities = None
        self.num_possibilities = None
        self.initialise_possibilities() # Don't really want to have to do this for nongreedy methods


    def is_legal_move(self, num, i, j):
        """
        Checks to see if num is already present in the row / col / local square \
            defined by (i, j) position of input
        """
        args = (self.grid, num, i, j)
        return (not check_row(*args)) and (not check_col(*args)) and (not check_local_square(*args))


    def find_next_empty_cell(self):
        """
        Finds the (row, col) of the next available unlabelled cell.
        Returns None if grid is complete
        """
        for i, row in enumerate(self.grid):
            for j, col in enumerate(row):
                if col == 0:
                    yield (i, j)
        return None


    def initialise_possibilities(self):
        """
        Removes illegal moves from opening grid
        0. Initialise grid_possibilities and num_possibilities attributes
        1. Finds next zero entry
        2. Eliminate impossible moves
        3. Counts the number of possible moves and stores this in num_possibilities
        """
        self.grid_possibilities = np.dstack([np.zeros_like(self.grid)] * self.size)
        self.num_possibilities = self.size * np.ones_like(self.grid)

        cell_generator = self.find_next_empty_cell()
        for cell in cell_generator:
            count = 0
            for val in range(self.size + 1):
                if self.is_legal_move(val, *cell):
                    self.grid_possibilities[cell[0]][cell[1]][val - 1] = 1
                    count += 1
            self.num_possibilities[cell[0]][cell[1]] = count


    def find_best_empty_cell(self):
        """
        Finds the (row, col) of a cell that has the lowest number of legal moves (randomly if more than one)
        Returns None if grid is complete
        TODO:
        This function needs testing
        """
        best = np.argwhere(self.num_possibilities == np.min(self.num_possibilities))
        if len(best) > 1:
            best = best[np.random.choice(best.shape[0], size=1)]
        return (best[0][0], best[0][1]) if self.num_possibilities[best[0][0]][best[0][1]] != self.size else None


    def update_grid(self, num, i, j):
        """
        Updates grid and possibilities given we attempt to place num in position (i, j)
        """
        self.grid[i][j] = num
        self.grid_possibilities[i][j][num] = 0
        self.num_possibilities[i][j] = self.size  # Max this out so it does not get picked again

        affected_cells = find_affected_cells(i, j)
        for cell in affected_cells:
            possibility = self.grid_possibilities[cell[0]][cell[1]][num]
            if possibility:
                self.grid_possibilities[cell[0]][cell[1]][num] = 0


    def revert_grid(self, num, i, j):
        """
        Reverts grid and possibilities to state before attempt to place num in position (i, j)
        """
        self.grid[i][j] = 0
        possibilities = self.find_possibilities(i, j)
        self.grid_possibilities[i][j] = possibilities
        self.num_possibilities[i][j] = len(possibilities)

        affected_cells = find_affected_cells(i, j)
        for cell in affected_cells:
            legal = check_position_is_legal(self.grid, num, i, j)
            if legal:
                self.grid_possibilities[cell[0]][cell[1]][num] = 1
        

    def find_possibilities(self, i, j):
        """
        Finds the possible values in a given cell (i, j)
        """
        possibilities = []
        for val in range(1, self.size + 1):
            legal = check_position_is_legal(self.grid, val, i, j)
            if legal:
                possibilities.append(1)
            else:
                possibilities.append(0)
        return np.array(possibilities)


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


def main():
    grid = intermediate
    b = Board(grid)
    b.display_board()
    p = b.grid_possibilities
    print(p.shape)
    a = b.num_possibilities
    print(a)
    q = b.find_best_empty_cell()
    print(q)

if __name__ == '__main__':
    main()