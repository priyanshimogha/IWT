def is_valid(board, row, col, num):
    # Check if num not in row
    if num in board[row]:
        return False

    # Check if num not in column
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check if num not in 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False

    return True

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c  # return position of empty cell
    return None

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True  # No empty cells, puzzle solved

    row, col = empty

    for num in range(1, 10):  # Try numbers 1 to 9
        if is_valid(board, row, col, num):
            board[row][col] = num  # Tentatively place number

            if solve_sudoku(board):  # Recursively solve
                return True

            board[row][col] = 0  # Backtrack if failed

    return False  # Trigger backtracking

def print_board(board):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("| ", end="")
            print(board[r][c] if board[r][c] != 0 else ".", end=" ")
        print()

# Example Sudoku (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print("Original Sudoku:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists!")
