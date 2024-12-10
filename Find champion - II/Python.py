# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Track the number of incoming edges for each node
        incoming = [0] * n

        # Count incoming edges for each node
        for src, dst in edges:
            incoming[dst] += 1

        # Step 2: Identify nodes with no incoming edges
        champions = []
        for i, incoming_cnt in enumerate(incoming):
            if incoming_cnt == 0:  # If a node has no incoming edges, it is a potential champion
                champions.append(i)

        # Step 3: Return the result
        if len(champions) > 1:
            return -1  # More than one champion found, return -1
        if not champions:
            return -1  # No champions found, return -1

        return champions[0]  # Exactly one champion found, return its index

