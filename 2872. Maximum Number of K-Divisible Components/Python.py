from collections import defaultdict
from typing import List

class Solution:
    def maxsplits(self, graph, i, prev, k, values):
        res = 0  # Count of k-divisible components
        curr = values[i]  # Start with the current node value

        # Traverse all adjacent nodes (children in DFS)
        for j in graph[i]:
            if j != prev:  # Skip parent node
                ncurr, nres = self.maxsplits(graph, j, i, k, values)
                curr += ncurr  # Add the remainder from child
                curr %= k  # Take modulo to avoid large numbers
                res += nres  # Add the number of divisible components from child

        # If the cumulative sum at this node is divisible by k
        if curr % k == 0:
            res += 1  # Increment component count
            curr = 0  # Reset remainder for this subtree

        return curr, res

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # Build the adjacency list for the tree
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # Start DFS from the root node (0), with -1 as the parent
        return self.maxsplits(graph, 0, -1, k, values)[1]
