import heapq
import math


def shortest_path(M, start, goal):
    # Heuristic function to calculate straight line distance between two nodes
    def heuristic(node1, node2):
        x1, y1 = M.intersections[node1]
        x2, y2 = M.intersections[node2]
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    # Function to reconstruct the path from the "came_from" dictionary
    def reconstruct_path(came_from, start, goal):
        path = [goal]
        current = goal
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    # Initialization of variables
    open_set = [(0, start)]  # heap with open nodes (f_score, node)
    closed_set = set()  # set with closed nodes
    g_score = {node: float('inf') for node in M.intersections}  # dictionary with actual cost to each node
    g_score[start] = 0  # the actual cost to the start node is 0
    came_from = {}  # dictionary to store the search tree

    # Main loop
    while len(open_set) > 0:
        _, current = heapq.heappop(open_set)  # get the node with lowest f_score from the open set
        if current == goal:
            path = reconstruct_path(came_from, start, goal)  # reconstruct the path from the search tree
            return path

        closed_set.add(current)  # add the current node to the closed set

        # Iterate through the neighbors of the current node
        for neighbor in M.roads[current]:
            if neighbor in closed_set:
                continue  # ignore nodes already explored

            tentative_g_score = g_score[current] + heuristic(current, neighbor)  # calculate the tentative g_score

            # If the tentative g_score is lower than the current g_score, update the neighbor node
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current  # update the search tree
                g_score[neighbor] = tentative_g_score  # update the g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)  # calculate the f_score
                heapq.heappush(open_set, (f_score, neighbor))  # add the neighbor node to the open set

    return None
