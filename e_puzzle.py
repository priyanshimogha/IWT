import random
import copy

# Function to find the position of the empty tile (0)
def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

# Function to move the empty tile in the specified direction
def move(board, direction):
    zero_pos = find_zero(board)
    if zero_pos is None:
        return None  # No empty tile found, move not possible
    i, j = zero_pos
    new_board = copy.deepcopy(board)  # Make a copy to avoid modifying the original board
    if direction == 'up' and i > 0:
        new_board[i][j], new_board[i-1][j] = new_board[i-1][j], new_board[i][j]
    elif direction == 'down' and i < 2:
        new_board[i][j], new_board[i+1][j] = new_board[i+1][j], new_board[i][j]
    elif direction == 'left' and j > 0:
        new_board[i][j], new_board[i][j-1] = new_board[i][j-1], new_board[i][j]
    elif direction == 'right' and j < 2:
        new_board[i][j], new_board[i][j+1] = new_board[i][j+1], new_board[i][j]
    else:
        return None  # Move not possible
    return new_board

# Function to generate all possible valid moves (neighbors)
def get_neighbors(board):
    neighbors = []
    directions = ['up', 'down', 'left', 'right']
    for direction in directions:
        neighbor = move(board, direction)
        if neighbor is not None:
            neighbors.append(neighbor)
    return neighbors

# Heuristic function: Number of misplaced tiles (excluding the empty tile)
def heuristic(board, goal):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0 and board[i][j] != goal[i][j]:
                misplaced += 1
    return misplaced

# Hill Climbing Algorithm
def hill_climbing(start, goal):
    current = start
    current_h = heuristic(current, goal)

    while True:
        neighbors = get_neighbors(current)

        # If no neighbors, we are stuck
        if not neighbors:
            break

        # Evaluate neighbors
        neighbor_scores = []
        for neighbor in neighbors:
            h = heuristic(neighbor, goal)
            neighbor_scores.append((h, neighbor))

        # Sort neighbors by heuristic value (lower is better)
        neighbor_scores.sort()

        best_h, best_neighbor = neighbor_scores[0]

        # If no better neighbor, stop
        if best_h >= current_h:
            break

        # Move to better neighbor
        current = best_neighbor
        current_h = best_h

        # If goal is reached
        if current_h == 0:
            break

    return current

# Function to print the board nicely
def print_board(board):
    for row in board:
        print(' '.join(str(x) if x != 0 else ' ' for x in row))
    print()

# Example usage
if __name__ == "__main__":
    # Initial configuration of the puzzle
    start = [
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]
    ]

    # Goal configuration of the puzzle
    goal = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]

    print("Starting Board:")
    print_board(start)

    # Solve using Hill Climbing
    result = hill_climbing(start, goal)

    print("Final Board After Hill Climbing:")
    print_board(result)
