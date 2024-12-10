# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import deque
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        m = len(grid)    # Number of rows
        n = len(grid[0]) # Number of columns

        # A deque (double-ended queue) to manage BFS traversal
        # Stores tuples in the form (x, y, d), where:
        #   x, y: Current cell coordinates
        #   d: Distance (or number of obstacles removed so far)
        q = deque([(0, 0, 0)])

        # A set to track visited cells
        v = {(0, 0)}  # Start with the top-left cell

        # Perform BFS
        while q:
            # Get the current cell and distance
            x, y, d = q.pop()

            # If the bottom-right cell is reached, return the number of obstacles removed
            if (x, y) == (m - 1, n - 1):
                return d

            # Explore all four possible directions: up, left, down, right
            for i, j in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]:
                # Check if the next cell is within bounds
                if 0 <= i < m and 0 <= j < n:
                    # Skip cells that have already been visited
                    if (i, j) in v:
                        continue

                    # Mark the cell as visited
                    v.add((i, j))

                    # If the next cell is an obstacle (grid[i][j] == 1)
                    if grid[i][j] == 1:
                        # Add it to the front of the deque with an increased distance
                        q.appendleft((i, j, d + 1))
                    else:
                        # If it's a free cell, add it to the back of the deque with the same distance
                        q.append((i, j, d))

        # If the target is not reachable, return -1 (though this is unlikely for a valid input)
        return -1
