import pytest
from Sudoku.Sudoku.tests import test_data
from Sudoku.Sudoku.src.utils import (find_next_empty_cell,
                                    check_row,
                                    check_col,
                                    check_local_square)

from Sudoku.Sudoku.src.board import Board

@pytest.mark.unit
class TestBoard:

    # @pytest.mark.parametrize(*test_data.)
    def test_is_legal_move(self, *args):
        pass 

    # @pytest.mark.parametrize(*test_data.)
    def test_initialize_possibilities(self, *args):
        pass
    
    @pytest.mark.parametrize(*test_data.test_find_best_empty_cell_data())
    def test_find_best_empty_cell(self, grid, expected):
        # Arrange
        board = Board(grid)

        # Act
        cell = board.find_best_empty_cell()

        # Assert
        assert cell == expected

    # @pytest.mark.parametrize(*test_data.)
    def test_update_grid(self, *args):
        pass 
    
    # @pytest.mark.parametrize(*test_data.)
    def test_revert_grid(self, *args):
        pass
    
    # @pytest.mark.parametrize(*test_data.)
    def test_find_possibilities(self, *args):
        pass

