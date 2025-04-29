import random

def print_board(state):
    n = len(state)
    board = []
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        board.append(line)
    print("\n".join(board))
    print()

def heuristic(state):
    """Number of attacking pairs."""
    h = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                h += 1
    return h

def get_neighbors(state):
    """Generate all possible neighbors by moving one queen in its column."""
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = list(state)
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

def hill_climbing(n):
    """Hill Climbing for N-Queens"""
    # Initial random state
    current = [random.randint(0, n - 1) for _ in range(n)]
    current_h = heuristic(current)
    steps = 0

    while True:
        neighbors = get_neighbors(current)
        next_state = None
        next_h = current_h

        for neighbor in neighbors:
            h = heuristic(neighbor)
            if h < next_h:
                next_h = h
                next_state = neighbor

        if next_state is None:
            # No better neighbor found
            break

        current = next_state
        current_h = next_h
        steps += 1

        if current_h == 0:
            break

    return current, current_h, steps

# Run
n = 8  # Change N here
solution, final_heuristic, steps = hill_climbing(n)

print(f"Solution found in {steps} steps with heuristic {final_heuristic}")
print_board(solution)
