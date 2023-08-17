# Import necessary modules
import pygame
from ressources.spot_class import Spot

def make_grid(rows, width):
    """
    Create a 2D grid of spots for pathfinding visualization.
    """
    grid = []
    gap = width // rows  # Determine the width and height of each individual spot in the grid
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)  # Initialize a new spot object
            grid[i].append(spot)  # Add the spot to the current row in the grid

    return grid

def h(p1, p2):
    """
    Calculate the Manhattan distance between two points.
    """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance

def reconstruct_path(came_from, current, draw):
    """
    Recreate the path from start to end after pathfinding has been completed.
    """
    while current in came_from:
        current = came_from[current]
        current.make_path()  # Update the spot's visual status to be part of the final path
        draw()  # Redraw the grid to visualize changes

def draw_grid(win, rows, width):
    """
    Draw grid lines on the window to distinguish individual spots.
    """
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, (128, 128, 128), (0, i * gap), (width, i * gap))  # Draw horizontal lines
        for j in range(rows):
            pygame.draw.line(win, (128, 128, 128), (j * gap, 0), (j * gap, width))  # Draw vertical lines

def draw(win, grid, rows, width):
    """
    Draw the entire grid and spots on the window.
    """
    win.fill((255, 255, 255))  # Fill the window with a white background

    for row in grid:
        for spot in row:
            spot.draw(win)  # Draw each spot on the window

    draw_grid(win, rows, width)  # Draw grid lines
    pygame.display.update()  # Update the window to display changes

def get_clicked_pos(pos, rows, width):
    """
    Convert pixel coordinates to grid row and column indices.
    """
    gap = width // rows
    y, x = pos

    row = y // gap  # Convert y-coordinate to row index
    col = x // gap  # Convert x-coordinate to column index

    return row, col
