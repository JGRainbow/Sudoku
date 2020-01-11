import pytest
from pytest import param

import numpy as np

def test_find_next_empty_cell_data():
    test_variables = "grid, expected"
    test_data = [
        param(
            np.array([
                [1,1,1],
                [1,1,1],
                [1,0,1]]),
                (2,1),
                id='simple_true'
        ),
        param(
            np.array([
                [1,1,1],
                [1,1,1],
                [1,1,1]]),
                None,
                id="no_empty_cells"
        )
    ]
    return (test_variables, test_data)

def test_check_row_data():
    test_variables = "grid, num, i, j, expected"
    test_data = [
        param(
            np.array([
                [1,2,3],
                [4,5,6],
                [7,8,9]]),
                6,
                1,
                1,
                True,
                id='found_on_row_true'
        ),
        param(
            np.array([
                [1,2,3],
                [4,5,6],
                [7,8,9]]),
                6,
                0,
                1,
                False,
                id="not_found_on_row_false"
            ),
        param(
            np.array([
                [1,2,3],
                [4,5,6],
                [7,8,9]]),
                6,
                1,
                2,
                False,
                id="found_on_row_in_current_cell_false"
        )       
    ]
    return test_variables, test_data

def test_check_col_data():
    test_variables = "grid, num, i, j, expected"
    test_data = [
        param(
            np.array([
                [1,2,3],
                [4,5,6],
                [7,8,9]]),
                4,
                0,
                0,
                True,
                id="found_in_col"
            ),
        param(
            np.array([
                [1,2,3],
                [4,5,6],
                [7,8,9]]),
                4,
                0,
                1,
                False,
                id="found_in_position"
        ),
        param(
            np.array([
                [1,2,3],
                [4,5,6],
                [7,8,9]]),
                4,
                0,
                1,
                False,
                id="not_found_in_col"
        )
    ]
    return test_variables, test_data

def test_check_local_square_data():
    test_variables = "grid, num, i, j, expected"
    test_data = [
        param(
            np.array([
                [0,0,0,0,0,3,6,0,0],
                [0,0,0,0,2,0,0,0,0],
                [0,3,9,8,0,0,0,0,1],
                [9,0,0,0,4,0,0,0,3],
                [3,4,0,6,0,2,0,8,0],
                [0,6,0,0,1,0,9,0,0],
                [0,8,0,0,0,0,2,0,0],
                [0,5,6,1,3,0,4,0,0],
                [4,0,0,0,8,7,0,0,0]
            ]),
            3,
            1,
            1,
            True,
            id="finds_value_in_top_corner"
        ),
        param(
            np.array([
                [0,0,0,0,0,3,6,0,0],
                [0,0,0,0,2,0,0,0,0],
                [0,3,9,8,0,0,0,0,1],
                [9,0,0,0,4,0,0,0,3],
                [3,4,0,6,0,2,0,8,0],
                [0,6,0,0,1,0,9,0,0],
                [0,8,0,0,0,0,2,0,0],
                [0,5,6,1,3,0,4,0,0],
                [4,0,0,0,8,7,0,0,0]
            ]),
            5,
            4,
            5,
            False,
            id="not_find_value_in_middle"
        ),
        param(
            np.array([
                [0,0,0,0,0,3,6,0,0],
                [0,0,0,0,2,0,0,0,0],
                [0,3,9,8,0,0,0,0,1],
                [9,0,0,0,4,0,0,0,3],
                [3,4,0,6,0,2,0,8,0],
                [0,6,0,0,1,0,9,0,0],
                [0,8,0,0,0,0,2,0,0],
                [0,5,6,1,3,0,4,0,0],
                [4,0,0,0,8,7,0,0,0]
            ]),
            3,
            7,
            4,
            False,
            id="find_value_in_current_position"
        )
    ]
    return test_variables, test_data
