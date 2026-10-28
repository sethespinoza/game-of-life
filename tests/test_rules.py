import pytest

from life.board import ALIVE, DEAD
from life.rules import count_live_neighbors, next_board_state, next_cell_state


def test_neighbor_counts_on_full_board():
    full = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    assert count_live_neighbors(full, 0, 0) == 3   # corner
    assert count_live_neighbors(full, 0, 1) == 5   # edge
    assert count_live_neighbors(full, 1, 1) == 8   # center


def test_cell_does_not_count_itself():
    board = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert count_live_neighbors(board, 1, 1) == 0


@pytest.mark.parametrize("current, neighbors, expected", [
    (ALIVE, 0, DEAD),    # underpopulation
    (ALIVE, 1, DEAD),
    (ALIVE, 2, ALIVE),   # survives
    (ALIVE, 3, ALIVE),
    (ALIVE, 4, DEAD),    # overpopulation
    (ALIVE, 8, DEAD),
    (DEAD, 2, DEAD),
    (DEAD, 3, ALIVE),    # reproduction
    (DEAD, 4, DEAD),
])
def test_cell_rules(current, neighbors, expected):
    assert next_cell_state(current, neighbors) == expected


def test_empty_board_stays_empty():
    board = [[0] * 4 for _ in range(4)]
    assert next_board_state(board) == board


def test_block_is_stable():
    block = [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]
    assert next_board_state(block) == block


def test_blinker_oscillates():
    vertical = [[0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0]]
    horizontal = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]
    assert next_board_state(vertical) == horizontal
    assert next_board_state(horizontal) == vertical


def test_cells_on_the_edge_follow_the_rules():
    top_row = [[1, 1, 1],
               [0, 0, 0],
               [0, 0, 0]]
    expected = [[0, 1, 0],
                [0, 1, 0],
                [0, 0, 0]]
    assert next_board_state(top_row) == expected


def test_input_board_is_not_modified():
    board = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    snapshot = [row[:] for row in board]
    next_board_state(board)
    assert board == snapshot