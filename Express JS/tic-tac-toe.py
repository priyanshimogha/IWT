import math

# Constants
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

# Create the board
def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

# Display the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check for winner
def check_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
        all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
    all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if board is full
def is_full(board):
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

# Alpha-Beta Pruning Minimax
def minimax(board, depth, alpha, beta, is_maximizing):
    if check_winner(board, AI):
        return 1
    if check_winner(board, HUMAN):
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Best move for AI
def best_move(board):
    best_val = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Main Game Loop
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human Move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if board[row][col] != EMPTY:
            print("Cell already occupied! Try again.")
            continue
        board[row][col] = HUMAN
        print_board(board)

        if check_winner(board, HUMAN):
            print("You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI Move
        print("AI's move:")
        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = AI
        print_board(board)

        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
