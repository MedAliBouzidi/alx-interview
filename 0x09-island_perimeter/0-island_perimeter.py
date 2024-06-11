#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid

    Arguments:
        grid: A list of list of integers

    Returns:
        The perimeter of the island described in grid
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
