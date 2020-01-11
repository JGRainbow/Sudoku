import pytest
from Sudoku.Sudoku.tests import test_data
from Sudoku.Sudoku.src.utils import (find_next_empty_cell,
                                    check_row,
                                    check_col,
                                    check_local_square)

@pytest.mark.unit
class TestUtils:

    @pytest.mark.parametrize(*test_data.test_find_next_empty_cell_data())
    def test_find_next_empty_cell(self, grid, expected):
        # Arrange

        # Act
        result = find_next_empty_cell(grid)

        # Assert
        assert result == expected

    @pytest.mark.parametrize(*test_data.test_check_row_data())
    def test_check_row(self, grid, num, i, j, expected):
        # Arrange

        # Act
        result = check_row(grid, num, i, j)

        # Assert
        assert result == expected 
