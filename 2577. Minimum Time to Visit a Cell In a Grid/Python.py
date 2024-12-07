# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

import heapq
import math
from typing import List

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # Dimensions of the grid
        m = len(grid)
        n = len(grid[0])

        # If both adjacent cells to the top-left corner are blocked initially, return -1
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        # A matrix to track the minimum time to reach each cell
        time = [[float('inf')] * n for _ in range(m)]
        time[0][0] = 0  # Start at the top-left corner with time 0

        # Min-heap to implement Dijkstra's algorithm; stores tuples of (time, row, column)
        heap = [(0, 0, 0)]  # Start with the initial cell

        # Perform the Dijkstra-like traversal
        while heap:
            d, i, j = heapq.heappop(heap)  # Get the cell with the smallest current time
            if (i, j) == (m - 1, n - 1):  # If we reach the bottom-right corner, return the time
                return d

            # Explore all four possible directions
            for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n:  # Ensure the next cell is within bounds
                    ntime = d + 1  # Increment time by 1 to move to the next cell

                    # If the current time does not allow moving to the cell due to its time constraint
                    if d + 1 < grid[x][y]:
                        diff = grid[x][y] - d - 1  # Calculate the time difference
                        # Adjust the time to the next valid moment we can move into the cell
                        ntime = d + 1 + 2 * math.ceil(diff / 2)

                    # If we found a shorter time to reach this cell, update and push to heap
                    if ntime < time[x][y]:
                        time[x][y] = ntime
                        heapq.heappush(heap, (ntime, x, y))

        # If we cannot reach the bottom-right corner, return -1
        return -1
