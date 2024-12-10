# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Step 1: Initialize adjacency list for graph edges
        edges = [[] for _ in range(n)]  # `edges[i]` contains the list of nodes that node `i` points to
        res = []  # To store results after each query

        # Step 2: Process each query
        for l, r in queries:
            # Add the new edge from `l` to `r`
            edges[l].append(r)

            # Step 3: Calculate shortest distances using dynamic programming
            dp = [float('inf')] * n  # Initialize distance array with infinity
            dp[n - 1] = 0  # Distance to the last node from itself is 0

            # Compute shortest distances from each node to the last node
            for i in range(n - 2, -1, -1):
                # Option 1: Take the edge to the next node (if it exists)
                dp[i] = min(dp[i], 1 + dp[i + 1])
                # Option 2: Use any edge from `i` to a specific node `r`
                for r in edges[i]:
                    dp[i] = min(dp[i], 1 + dp[r])

            # Step 4: Append the shortest distance from node 0 to node n-1 to the result
            res.append(dp[0])

        return res
