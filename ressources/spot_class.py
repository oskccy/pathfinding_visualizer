import pygame

class Spot:
    def __init__(self, row, col, width, total_rows):
        """
        Initialize a spot on the grid.

        Parameters:
        - row: Row number of the spot.
        - col: Column number of the spot.
        - width: Width of each spot (square size).
        - total_rows: Total number of rows in the grid.
        """
        self.row = row
        self.col = col
        # Calculate the pixel position based on the given row, column, and width.
        self.x = row * width
        self.y = col * width
        self.color = (255, 255, 255)  # Default color is white.
        self.neighbors = []  # List to store neighboring spots.
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        """Return the row and column of the spot."""
        return self.row, self.col

    # Following methods check the status of the spot based on its color.
    def is_closed(self):
        return self.color == (255, 0, 0)

    def is_open(self):
        return self.color == (0, 255, 0)

    def is_barrier(self):
        return self.color == (0, 0, 0)

    def is_start(self):
        return self.color == (255, 165 ,0)

    def is_end(self):
        return self.color == (64, 224, 208)

    def reset(self):
        """Reset the spot's color to default (white)."""
        self.color = (255, 255, 255)

    # Following methods change the status (color) of the spot.
    def make_start(self):
        self.color = (255, 165 ,0)

    def make_closed(self):
        self.color = (255, 0, 0)

    def make_open(self):
        self.color = (0, 255, 0)

    def make_barrier(self):
        self.color = (0, 0, 0)

    def make_end(self):
        self.color = (64, 224, 208)

    def make_path(self):
        self.color = (120, 0, 120)

    def draw(self, win):
        """
        Draw the spot on the given window.

        Parameters:
        - win: Pygame window object where the spot should be drawn.
        """
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        """
        Update the neighbors of the spot based on the given grid.

        Parameters:
        - grid: 2D list of Spot objects.
        """
        self.neighbors = []
        # Check below (DOWN) the current spot if it's not a barrier and is within bounds.
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # Check above (UP) the current spot.
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # Check to the right (RIGHT) of the current spot.
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # Check to the left (LEFT) of the current spot.
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        """Less than operator overloading. Currently returns False for any comparison."""
        return False
