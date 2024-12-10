# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import deque
from typing import List

# Precompute all possible states and their distances from the solved state
start = (1, 2, 3, 4, 5, 0)  # The solved state of the sliding puzzle
q = deque([(start, 0)])      # Queue for BFS, initialized with the solved state and distance 0
v = {start}                  # Set to keep track of visited states
res = {}                     # Dictionary to store the shortest distance to each state

# Perform BFS to calculate distances from the solved state
while q:
    curr, d = q.pop()  # Current state and its distance from the solved state
    res[curr] = d      # Record the distance for this state

    # Find the position of the empty tile (0)
    pos = curr.index(0)
    i, j = pos // 3, pos % 3  # Convert the position into (row, column) format

    # Explore all possible moves (up, left, down, right)
    for x, y in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        # Check if the move is within bounds
        if 0 <= x < 2 and 0 <= y < 3:
            # Create the new state by swapping tiles
            newcurr = list(curr)
            newcurr[pos], newcurr[3 * x + y] = newcurr[3 * x + y], newcurr[pos]
            newcurr = tuple(newcurr)  # Convert back to tuple for immutability

            # If the new state hasn't been visited, add it to the queue
            if newcurr not in v:
                v.add(newcurr)
                q.appendleft((newcurr, d + 1))  # Push with incremented distance

# Sliding Puzzle Solver Class
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Flatten the board into a single tuple and look up the precomputed result
        return res.get(tuple(board[0] + board[1]), -1)

