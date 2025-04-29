import random
import copy

# Starting Sudoku puzzle
initial_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Fill empty cells randomly inside each 3x3 box
def fill_grid(grid):
    new_grid = copy.deepcopy(grid)
    for box_row in range(3):
        for box_col in range(3):
            numbers = list(range(1, 10))
            for i in range(3):
                for j in range(3):
                    row = box_row * 3 + i
                    col = box_col * 3 + j
                    if new_grid[row][col] != 0:
                        numbers.remove(new_grid[row][col])
            # Fill remaining empty cells
            random.shuffle(numbers)
            for i in range(3):
                for j in range(3):
                    row = box_row * 3 + i
                    col = box_col * 3 + j
                    if new_grid[row][col] == 0:
                        new_grid[row][col] = numbers.pop()
    return new_grid

# Calculate score (number of conflicts)
def score(grid):
    conflicts = 0
    for i in range(9):
        conflicts += (9 - len(set(grid[i])))  # Row conflicts
        conflicts += (9 - len(set(row[i] for row in grid)))  # Column conflicts
    return conflicts

# Generate neighbors by swapping two numbers in the same 3x3 box
def get_neighbors(grid):
    neighbors = []
    for box_row in range(3):
        for box_col in range(3):
            cells = []
            for i in range(3):
                for j in range(3):
                    row = box_row * 3 + i
                    col = box_col * 3 + j
                    if initial_grid[row][col] == 0:
                        cells.append((row, col))
            for i in range(len(cells)):
                for j in range(i + 1, len(cells)):
                    new_grid = copy.deepcopy(grid)
                    (r1, c1), (r2, c2) = cells[i], cells[j]
                    new_grid[r1][c1], new_grid[r2][c2] = new_grid[r2][c2], new_grid[r1][c1]
                    neighbors.append(new_grid)
    return neighbors

# Hill Climbing for Sudoku
def hill_climb(grid):
    current = fill_grid(grid)
    while True:
        neighbors = get_neighbors(current)
        best_neighbor = min(neighbors, key=score)
        if score(best_neighbor) < score(current):
            current = best_neighbor
        else:
            break
    return current

# Start
solution = hill_climb(initial_grid)
for row in solution:
    print(row)
print("Conflicts:", score(solution))
