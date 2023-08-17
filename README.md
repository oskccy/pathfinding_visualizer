# Path Finding Algorithm Visualizer

This project visualizes the A* pathfinding algorithm using the Pygame library. Users can interactively set start and end points, create barriers, and see the optimal path formed in real-time.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Features](#features)
3. [Usage](#usage)
4. [File Structure](#file-structure)
5. [Spot Class](#spot-class)
6. [A* Algorithm](#a-algorithm)

## Prerequisites

- Python 3.x
- Pygame (pip install pygame)

## Features

- Interactive GUI to set start and end points.
- Ability to create barriers.
- Visualization of the A* algorithm in action.
- Clear board and reset functionality.

## Usage

1. Run `main.py` to start the application.
2. Left-click to set the start (Goldenrod color) and end points (Deep Sky Blue).
3. Continue left-clicking to set barriers (Dark Gray).
4. Right-click on any spot to reset its state.
5. Press `SPACE` to start the algorithm once the start and end points are set.
6. Press `C` to clear the entire board and reset.

## File Structure

- `main.py`: The main driver of the program that contains the GUI and handles user inputs.

## Spot Class

The `Spot` class is used to represent each cell on the grid. The various functionalities of the `Spot` class include:

- Determining the state (start, end, open, closed, barrier).
- Drawing itself on the Pygame window.
- Updating its neighbors.
- Checking neighboring cells for barriers.

## A* Algorithm

The implementation utilizes the A* (A-Star) algorithm which uses a heuristic to find the shortest path from the start node to the end node. The specific heuristic used is the Manhattan distance.

The `algorithm` function carries out the A* search and the `reconstruct_path` function is used to backtrack from the end node to the start node, displaying the optimal path.

---

**Note**: Ensure that the Pygame library is installed and the main method is located in `main.py` before running.

Happy Pathfinding!
