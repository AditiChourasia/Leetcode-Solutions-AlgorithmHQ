# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the graph and track in-degrees and out-degrees of nodes.
        graph = defaultdict(list)  # Adjacency list for the directed graph.
        degree = defaultdict(int)  # Tracks the degree difference (out-degree - in-degree).

        for x, y in pairs:
            graph[x].append(y)  # Add directed edge from x to y.
            degree[x] += 1      # Increment out-degree of x.
            degree[y] -= 1      # Decrement in-degree of y.

        # Step 2: Find the starting node for the Eulerian Path.
        # If a node has degree[k] == 1, it will be the starting node.
        for k in degree:
            if degree[k] == 1:
                x = k  # Found the starting node.
                break
        else:
            # If no specific starting node is found, pick any node from the pairs.
            x = pairs[0][0]

        # Step 3: Initialize the result list.
        ans = []

        # Step 4: Define the function for Hierholzer's Algorithm to find the Eulerian Path.
        def fn(x):
            # While there are edges from the current node
            while graph[x]:
                # Recursively explore the next edge
                fn(graph[x].pop())
            # Add the node to the result once all outgoing edges are visited
            ans.append(x)

        # Start the DFS traversal from the chosen starting node.
        fn(x)

        # Step 5: Reverse the order to construct the path.
        ans.reverse()

        # Step 6: Convert the node sequence into edge pairs.
        return [[ans[i], ans[i + 1]] for i in range(len(ans) - 1)]
