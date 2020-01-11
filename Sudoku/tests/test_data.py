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
