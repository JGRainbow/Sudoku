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

def main():
    grid = easy
    solver = Solver(grid)
    solver.solve()

if __name__ == '__main__':
    main()