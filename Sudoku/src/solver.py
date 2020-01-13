import numpy as np

from board import Board
from data import easy, intermediate
from utils import find_next_empty_cell
from decorators import timer

class Solver:

    """
    Generic Solver class that takes a board and runs various algorithms to solve it
    """

    def __init__(self, grid):
        self.board = Board(grid)
        self.size = self.board.grid.shape[0]

    @timer
    def solve(self):
        """
        Non-recursive formulation so we can time it
        """
        if self.basic_backtracker():
            self.board.display_board()
        else:
            print('No solution exists!')

    def basic_backtracker(self):
        """
        Attempts to solve Sudoku using backtracking algorithm

        # 1. See if board is already complete
        # 2. Find first missing entry
        # 3. Try all possibilities until legal move is found
        # 4. If no legal move, backtrack
        # 5. If legal move, then update board and see if it is solvable
        """
        cell = find_next_empty_cell(self.board.grid)
        if not cell:
            return True

        for val in range(1, self.size + 1):
            legal = self.board.is_legal_move(val, *cell)
            if legal:
                self.board.grid[cell[0]][cell[1]] = val 

                if self.basic_backtracker():
                    return True

                self.board.grid[cell[0]][cell[1]] = 0

        return False  


    def greedy_backtracker(self):
        """
        Adapts basic backtracker by targeting cells with the current least \
            number of legal possibilities
        TODO: Something is broken (allowing illegal moves)
        """
        cell = self.board.find_best_empty_cell()
        print(cell)
        if not cell:
            return True

        legal_moves = np.where(self.board.grid_possibilities[cell[0]][cell[1]] == 1)[0]
        for val in legal_moves:
            print(f'Attempting Val: {val}')
            self.board.update_grid(val, *cell)
         
            if self.greedy_backtracker():
                print(f'placing {val} in position {cell}')
                return True
            
            self.board.revert_grid(val, *cell)

        return False

def main():
    grid = intermediate
    solver = Solver(grid)
    # solver.solve()
    solver.greedy_backtracker()

    solver.board.display_board()

if __name__ == '__main__':
    main()