import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tic_tac_toe import check_winner, new_board, best_move, EMPTY


def test_empty_board():
    b = new_board()
    for row in b:
        for cell in row:
            assert cell == EMPTY


def test_row_win():
    b = new_board()
    b[0] = ["X", "X", "X"]
    assert check_winner(b) == "X"


def test_col_win():
    b = new_board()
    b[0][1] = "O"
    b[1][1] = "O"
    b[2][1] = "O"
    assert check_winner(b) == "O"


def test_diagonal_win():
    b = new_board()
    b[0][0] = "X"
    b[1][1] = "X"
    b[2][2] = "X"
    assert check_winner(b) == "X"


def test_anti_diagonal_win():
    b = new_board()
    b[0][2] = "O"
    b[1][1] = "O"
    b[2][0] = "O"
    assert check_winner(b) == "O"


def test_draw():
    b = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"],
    ]
    assert check_winner(b) == "Draw"


def test_game_still_going():
    b = new_board()
    b[0][0] = "X"
    # nobody's won yet and board isn't full, so this should be None
    assert check_winner(b) is None


def test_ai_blocks_when_about_to_lose():
    b = new_board()
    b[0][0] = "X"
    b[0][1] = "X"
    # X is one move away from winning the top row, ai (O) needs to block at (0,2)
    assert best_move(b) == (0, 2)


def test_ai_takes_the_win_if_its_there():
    b = new_board()
    b[0][0] = "O"
    b[0][1] = "O"
    b[1][0] = "X"
    b[1][1] = "X"
    assert best_move(b) == (0, 2)
