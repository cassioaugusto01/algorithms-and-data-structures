import heapq
from math import sqrt

def shortest_path(M, start, goal):
    # Euclidean distance heuristic function
    def euclidean_distance(a, b):
        return sqrt((M.intersections[a][0] - M.intersections[b][0])**2 + (M.intersections[a][1] - M.intersections[b][1])**2)

    # Alternative heuristic functions:

    # Manhattan distance heuristic function
    # This function computes the sum of the absolute differences in the x and y coordinates.
    # It works well in grid-like environments where movement is restricted to horizontal and vertical directions.
    # def manhattan_distance(a, b):
    #     return abs(M.intersections[a][0] - M.intersections[b][0]) + abs(M.intersections[a][1] - M.intersections[b][1])

    # Diagonal distance heuristic function
    # This function computes the distance by taking into account diagonal movements.
    # It is useful when diagonal movements are allowed in the environment.
    # def diagonal_distance(a, b):
    #     dx = abs(M.intersections[a][0] - M.intersections[b][0])
    #     dy = abs(M.intersections[a][1] - M.intersections[b][1])
    #     return min(dx, dy) * sqrt(2) + abs(dx - dy)

    # Function to reconstruct the final path
    # This function takes the 'came_from' dictionary and the current node as input,
    # then iteratively traces back from the goal node to the start node using the dictionary.
    # The resulting path is then reversed and returned as a list.
    def reconstruct_path(came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        return path[::-1]

    # Initialize the open set with the start node and the closed set as an empty set
    # The open set stores nodes that are to be evaluated, whereas the closed set stores nodes that have already been evaluated.
    open_set = [(euclidean_distance(start, goal), 0, start)]
    closed_set = set()
    came_from = {}
    g_score = {start: 0}

    # Main loop for the A* search algorithm
    while open_set:
        # Get the node with the lowest total cost (f_score) from the open set
        _, current_g, current = heapq.heappop(open_set)

        # If the current node is the goal node, the search is successful, and the path is reconstructed and returned
        if current == goal:
            return reconstruct_path(came_from, current)

        # Mark the current node as evaluated by adding it to the closed set
        closed_set.add(current)

        # Iterate through each neighbor of the current node
        for neighbor in M.roads[current]:
            # Calculate the tentative cost (g_score) from the start node to the neighbor through the current node
            tentative_g_score = current_g + euclidean_distance(current, neighbor)

            # If the neighbor has already been evaluated and the tentative cost is not better than its current g_score,
            # skip this neighbor
            if neighbor in closed_set and tentative_g_score >= g_score.get(neighbor, float("inf")):
                continue

            # If the tentative cost is better than the current g_score of the neighbor,
            # update the came_from dictionary, g_score, and push the neighbor into the open set
            if tentative_g_score < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + euclidean_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g_score, neighbor))

    return None
               
