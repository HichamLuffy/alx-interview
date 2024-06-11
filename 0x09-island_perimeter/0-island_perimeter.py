#!/usr/bin/python3
""" island primeter """


def island_perimeter(grid):
    """ island perimeter """
    perimeter = 0

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Define the directions for neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Traverse each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # For each land cell, check its neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check if the neighbor is out of bounds or water
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                        perimeter += 1

    return perimeter
