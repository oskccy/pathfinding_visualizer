import pygame
from queue import PriorityQueue

# Import helper functions for reconstructing the path and computing the heuristic
from ressources.helper_functions import reconstruct_path, h

def algorithm(draw, grid, start, end):
    """
    Implement the A* pathfinding algorithm.
    """
    count = 0
    open_set = PriorityQueue()  # Priority queue to prioritize nodes with lower costs
    open_set.put((0, count, start))  # Initial node: (cost, count, node)
    
    came_from = {}  # To store the path
    
    # Start with all nodes having infinite cost
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0  # Starting node's cost is 0

    # Start with all nodes having infinite estimated cost to the target
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())  # Heuristic cost for starting node

    open_set_hash = {start}  # Using a set to keep track of items in the priority queue for O(1) lookup

    while not open_set.empty():
        # Check for pygame events like quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]  # Get the node with the smallest cost from the queue
        open_set_hash.remove(current)  # Remove it from our set

        # If the current node is the end node, reconstruct and display the path
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        # Check all neighbors of the current node
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1  # Temporary g score considering moving from current to this neighbor

            # If this path to the neighbor is shorter than any previously known paths, update
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current  # Update optimal predecessor
                g_score[neighbor] = temp_g_score  # Update g score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())  # Update total cost (g+h)
                
                # If the neighbor hasn't been considered yet, add it to the open set
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()  # Update the visualization

        # If the current node is not the starting node, mark it as visited
        if current != start:
            current.make_closed()

    return False  # Return false if no path was found
