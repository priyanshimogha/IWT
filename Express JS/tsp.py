# import sys

# def tsp_minmax(graph, visited, current_city, count, cost, start_city):

#     # base case
#     if count == len(graph):
#         return cost + graph[current_city][start_city]
    
#     min_cost = sys.maxsize

#     # try all cities
#     for city in range(len(graph)):
#         if not visited[city]:
#             visited[city] = True
#             total_cost = tsp_minmax(
#                 graph,
#                 visited,
#                 city,
#                 count + 1,
#                 cost + graph[current_city][city],
#                 start_city
#             )
#             min_cost = min(min_cost, total_cost)
#             visited[city] = False 
        
#     return min_cost
    
# def solve_tsp(graph):
#     n = len(graph)
#     visited = [False] * n
#     start_city = 0
#     visited[start_city] = True

#     min_total_cost = tsp_minmax(graph, visited, start_city, 1, 0, start_city)
#     return min_total_cost

# graph = [
#     [0, 10, 15, 20],  
#     [10, 0, 35, 25],  
#     [15, 35, 0, 30],  
#     [20, 25, 30, 0]   
# ]

# answer = solve_tsp(graph)
# print("Minimum cost of travelling: ", answer)

import sys

def tsp_minmax(graph, visited,count, start_city, current_city, cost):
    # base case 
    if count == len(graph):
        return cost + graph[current_city][start_city]
    
    min_cost = sys.maxsize

    for city in range(len(graph)):
        if not visited[city]:
            visited[city] = True
            total_cost = tsp_minmax(
                graph,
                visited,
                count + 1,
                start_city,
                city,
                cost + graph[current_city][city]
            )
            min_cost = min(min_cost, total_cost)
            visited[city] = False

    return min_cost

def solve_tsp(graph):
    n = len(graph)
    visited = [False] * n
    start_city = 0
    visited[start_city] = True

    min_total_cost = tsp_minmax(graph, visited, 1, start_city, start_city, 0)
    return min_total_cost

graph = [
    [0, 10, 15, 20],  
    [10, 0, 35, 25],  
    [15, 35, 0, 30],  
    [20, 25, 30, 0]   
]

answer = solve_tsp(graph)
print("minimum cost of travelling", answer)