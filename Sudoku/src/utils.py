# from board import Board
from Sudoku.Sudoku.src.board import Board
from Sudoku.Sudoku.src.data import easy
from Sudoku.Sudoku.src.display import pretty_display
# from data import easy
# from display import pretty_display

def find_next_empty_cell(grid):
    """
    Finds the (row, col) of the next available unlabelled cell
    Returs None if grid is complete
    """
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 0:
                return (i, j)
    return None 

def check_row(grid, num, i, j):
    """
    Checks to see if num is already present somewhere in the row defined by (i, j) position of input
    """
    assert i < len(grid), 'Row is out of grid!'
    assert j < len(grid[0]), 'Column is out of grid!'

    found = False
    for col in range(len(grid[i])):
        if grid[i][col] == num and col != j:
            found = True
    return found
    
def check_col(grid, num, i, j):
    """
    Checks to see if num is already present somewhere in the col defined by (i, j) position of input
    """
    assert i < len(grid), 'Row is out of grid!'
    assert j < len(grid[0]), 'Column is out of grid!'    

    found = False
    for pos, row in enumerate(grid):
        if row[j] == num and pos != i:
            found = True
    return found 


def check_local_square(grid, num, i, j):
    """
    Checks to see if num is already present somewhere in the mini-square defined by (i, j) position of input
    """
    assert i < len(grid), 'Row is out of grid!'
    assert j < len(grid[0]), 'Column is out of grid!'    


pretty_display(easy)
t = find_next_empty_cell(easy)
print(t)

