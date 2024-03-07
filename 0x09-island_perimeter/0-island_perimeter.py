#!/usr/bin/python3
"""island perimater"""


def island_perimeter(grid):
    """island perimeter"""
    if type(grid) != list:
        return 0
    perimeter = 0
    for i in range(1, len(grid)):
        for j in range(1, len(grid[i])):
            current = grid[i][j]
            if current == 1:
                # check the top
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
    return perimeter
