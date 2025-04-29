import random

# Heuristic: Number of misplaced tiles
def heuristic(state, goal):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

# Get possible moves
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    x, y = divmod(idx, 3)

    moves = {
        'UP': (x-1, y),
        'DOWN': (x+1, y),
        'LEFT': (x, y-1),
        'RIGHT': (x, y+1)
    }

    for move, (nx, ny) in moves.items():
        if 0 <= nx < 3 and 0 <= ny < 3:
            n_idx = nx * 3 + ny
            new_state = list(state)
            new_state[idx], new_state[n_idx] = new_state[n_idx], new_state[idx]
            neighbors.append((tuple(new_state), move))
    return neighbors

# Hill Climbing Algorithm
def hill_climbing(start, goal):
    current = start
    path = []

    while True:
        current_h = heuristic(current, goal)
        if current_h == 0:
            return path  # reached goal!

        neighbors = get_neighbors(current)
        neighbors_h = [(heuristic(neigh, goal), neigh, move) for neigh, move in neighbors]
        neighbors_h.sort()

        best_h, best_neighbor, best_move = neighbors_h[0]

        if best_h >= current_h:
            # No improvement → local maxima
            return None

        # Move to better neighbor
        current = best_neighbor
        path.append(best_move)

# Display Puzzle
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Main
if __name__ == "__main__":
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    goal = (1, 2, 3,
            4, 5, 6,
            7, 8, 0)

    print("Initial State:")
    print_puzzle(start)

    path = hill_climbing(start, goal)

    if path:
        print("Solution found in", len(path), "moves:")
        print(path)
    else:
        print("Failed to reach goal — stuck at local maxima!")
