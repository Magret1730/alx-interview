#!/usr/bin/python3
""" Island Perimeter """

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    if not grid or not grid[0]:
        return 0
    
    def count_perimeter(i, j):
        """
        Counts the perimeter contributions of a land cell at (i, j).
        """
        perimeter = 0
        # Check the four directions
        if i == 0 or grid[i-1][j] == 0:
            perimeter += 1  # Up edge
        if i == len(grid) - 1 or grid[i+1][j] == 0:
            perimeter += 1  # Down edge
        if j == 0 or grid[i][j-1] == 0:
            perimeter += 1  # Left edge
        if j == len(grid[0]) - 1 or grid[i][j+1] == 0:
            perimeter += 1  # Right edge
        return perimeter

    total_perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                total_perimeter += count_perimeter(i, j)
    
    return total_perimeter
