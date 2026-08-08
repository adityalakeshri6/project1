import math

EMPTY = "_"

def new_board():
    return [[EMPTY, EMPTY, EMPTY] for _ in range(3)]

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print()

def check_winner(board):
    # check rows and cols
    for i in range(3):
        if board[i][0] != EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != EMPTY and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    # still empty spots left -> game not over yet
    for row in board:
        if EMPTY in row:
            return None

    return "Draw"

def minimax(board, maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if winner == "Draw":
        return 0

    if maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = EMPTY
                    if score > best:
                        best = score
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = EMPTY
                    if score < best:
                        best = score
        return best

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def best_move_as_x(board):
    # same idea but for when the ai has to play X (minimizing side)
    best_score = math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = "X"
                score = minimax(board, True)
                board[i][j] = EMPTY
                if score < best_score:
                    best_score = score
                    move = (i, j)
    return move

def get_human_move(board):
    while True:
        try:
            row = int(input("row (0-2): "))
            col = int(input("col (0-2): "))
        except ValueError:
            print("that's not a number, try again")
            continue

        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("has to be 0, 1 or 2")
            continue

        if board[row][col] != EMPTY:
            print("that spot's taken")
            continue

        return row, col

def choose_symbol():
    while True:
        c = input("play as X or O? (X goes first) ").strip().upper()
        if c in ("X", "O"):
            return c
        print("just type X or O")

def play_round(human_symbol):
    ai_symbol = "O" if human_symbol == "X" else "X"
    board = new_board()
    print_board(board)

    turn = "X"  # X always starts no matter who's human
    while True:
        if turn == human_symbol:
            row, col = get_human_move(board)
            board[row][col] = human_symbol
        else:
            print("ai's thinking...")
            if ai_symbol == "O":
                move = best_move(board)
            else:
                move = best_move_as_x(board)
            board[move[0]][move[1]] = ai_symbol

        print_board(board)

        result = check_winner(board)
        if result:
            if result == "Draw":
                print("draw game")
            elif result == human_symbol:
                print("you win!")
            else:
                print("ai wins")
            return

        turn = "O" if turn == "X" else "X"

def play_game():
    print("tic tac toe - good luck beating the ai (you won't, best case is a draw)\n")
    while True:
        sym = choose_symbol()
        play_round(sym)
        again = input("play again? y/n ").strip().lower()
        if again != "y":
            print("thanks for playing")
            break

if __name__ == "__main__":
    play_game()
