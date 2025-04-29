import random
import math

# Coordinates of cities
cities = {
    0: (0, 0),
    1: (1, 5),
    2: (5, 2),
    3: (6, 6),
    4: (8, 3)
}

# Function to calculate distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Function to calculate total distance of a path (tour)
def total_distance(path):
    dist = 0
    for i in range(len(path)):
        dist += distance(path[i], path[(i + 1) % len(path)])  # Wrap around to starting city
    return dist

# Function to generate neighboring solutions by swapping two cities
def get_neighbors(path):
    neighbors = []
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            neighbor = path[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]  # Swap two cities
            neighbors.append(neighbor)
    return neighbors

# Hill Climbing algorithm
def hill_climb(path):
    current_path = path
    while True:
        neighbors = get_neighbors(current_path)
        best_neighbor = min(neighbors, key=total_distance)  # Find neighbor with least distance
        if total_distance(best_neighbor) < total_distance(current_path):
            current_path = best_neighbor
        else:
            break  # No improvement, so stop
    return current_path

# Starting point
initial_path = list(cities.keys())
random.shuffle(initial_path)  # Random initial tour
print("Initial path:", initial_path)
print("Initial distance:", total_distance(initial_path))

# Apply hill climbing
best_path = hill_climb(initial_path)
print("Best path found:", best_path)
print("Total distance of best path:", total_distance(best_path))
