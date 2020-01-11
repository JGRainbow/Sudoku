import numpy as np 
from data import easy

def pretty_row(arr):
    assert arr.shape == (9,), 'not valid Sudoku row'
    row = []
    for i, v in enumerate(arr):
        if i == 3 or i == 6:
            print('| ', end='')
        print(f'{v} ', end='')
    return row

def pretty_display(grid):
    assert grid.shape == (9, 9), 'not valid Sudoku grid shape'
    for i, row in enumerate(grid):
        if i == 3 or i == 6:
            print('---------------------')
        pretty_row(row)
        print('\r')

if __name__ == '__main__':
    c = pretty_display(easy)  
