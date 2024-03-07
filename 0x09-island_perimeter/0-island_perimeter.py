#!/usr/bin/python3
"""module to solve island perimeter"""


def island_perimeter(grid):
    """method to solve island perimeter"""
    R,C = len(grid), len(grid[0])
    perimeter = 0
    # Traverse the grid
    for i in range(R):
        for j in range(C):
            # If it is a land block increment perimeter by 4
            if grid[i][j] == 1:
                count = 0
                # Check whether top neighbour is a land and increment it by 1
                # as it intersects
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    count += 1 
                # Check whether left neighbour is a land and increment it by 1
                # as it intersects
                if j - 1 >= 0 and grid[i][j-1] == 1:
                     count += 1
                # Check whether bot neighbour is a land and increment it by 1
                # as it intersects
                if i + 1 < R and grid[i + 1][j] == 1:
                    count += 1 
                # Check whether right neighbour is a land and increment it by 1
                # as it intersects
                if j + 1 < C and grid[i][j + 1] == 1:
                     count += 1
                perimeter += 4 - count
    return perimeter
