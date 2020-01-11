from data import easy
from display import pretty_display 

class Board:
    """
    Very generic Board class to hold unsolved grid
    """
    
    def __init__(self, grid):
        self.grid = grid
        self.size = grid.shape[0]

    def display_board(self):
        pretty_display(self.grid)

def main():
    b = Board(easy)
    b.display_board()

if __name__ == '__main__':
    main()