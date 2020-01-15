# from data import easy

def find_next_empty_cell(grid):
    """
    Finds the (row, col) of the next available unlabelled cell
    Returns None if grid is complete
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

    MINI_GRID_SIZE = 3

    top_left_row = MINI_GRID_SIZE * (i // MINI_GRID_SIZE)
    top_left_col = MINI_GRID_SIZE * (j // MINI_GRID_SIZE)

    found = False
    for row in range(top_left_row, top_left_row + MINI_GRID_SIZE):
        for col in range(top_left_col, top_left_col + MINI_GRID_SIZE):
            if grid[row][col] == num and (row, col) != (i, j):
                found = True 
    return found


def check_position_is_legal(grid, num, i, j):
    """
    Checks to see if num is already present in the row / col / mini-square defined by (i, j) position of input
    """
    args = (grid, num, i, j)
    return (not check_row(*args)) and (not check_col(*args)) and (not check_local_square(*args))


def find_affected_cells(i, j):
    """
    Returns a list of cells in the same row / col / local square of the form [(a, b), ... , (c, d)]
    Does not include reference cell itself (i, j)
    TODO: This currently assumes standard Sudoku board shape
    """
    GRID_SIZE = 9
    MINI_GRID_SIZE = 3
    cells = set()
    
    # Cells in same row
    for row_idx in range(GRID_SIZE):
        cells.add((row_idx, j))

    # Cells in same col
    for col_idx in range(GRID_SIZE):
        cells.add((i, col_idx))

    # Cells in local square
    top_left_row = MINI_GRID_SIZE * (i // MINI_GRID_SIZE)
    top_left_col = MINI_GRID_SIZE * (j // MINI_GRID_SIZE)

    for row_idx in range(top_left_row, top_left_row + 3):
        for col_idx in range(top_left_col, top_left_col + 3):
            cells.add((row_idx, col_idx))

    # Remove reference cell itself
    cells.remove((i, j))

    return cells


