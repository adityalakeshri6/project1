# project1
A basic Tic Tac Toe game
# Tic-Tac-Toe Game with Minimax AI

import math

# Display the board
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

# Check for winner or draw
def check_winner(board):
    # Rows and Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "_":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "_":
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "_":
        return board[0][2]

    # Draw
    for row in board:
        if "_" in row:
            return None
    return "Draw"

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = "_"
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = "_"
                    best_score = min(score, best_score)
        return best_score

# AI Best Move
def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = "_"
                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move

# Main Game
def play_game():
    board = [["_", "_", "_"],
             ["_", "_", "_"],
             ["_", "_", "_"]]

    print("Welcome to Tic-Tac-Toe!")
    print("You are X | AI is O")
    print_board(board)

    while True:
        # User move
        while True: # Added a loop for user input validation
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))

                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Invalid input! Row and column must be between 0 and 2. Please try again.")
                    continue

                if board[row][col] != "_":
                    print("Invalid move! Position already taken. Please try again.")
                    continue
                break # Exit input validation loop if input is valid
            except ValueError:
                print("Invalid input! Please enter a single digit number for row and column (e.g., 0, 1, or 2). Please try again.")

        board[row][col] = "X"
        print_board(board)

        if check_winner(board):
            break

        # AI move
        print("AI is making a move...")
        i, j = best_move(board)
        board[i][j] = "O"

        print_board(board)

        if check_winner(board):
            break

    result = check_winner(board)
    if result == "Draw":
        print("Game Over! It's a draw!")
    else:
        print("Game Over! Winner:", result)

play_game()
