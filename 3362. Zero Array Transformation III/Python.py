# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

import heapq
from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = len(queries)

        # Min-heap for currently active queries by end time
        min_heap = []

        # Max-heap for storing queries that start at the current index
        max_heap = []

        # Sort queries by start time
        queries.sort(key=lambda x: x[0])

        j = 0              # Pointer for queries
        usedQueries = 0    # Count of used queries

        for i in range(n):
            # Push queries that start at index i into max-heap (by end time descending)
            while j < q and queries[j][0] == i:
                heapq.heappush(max_heap, -queries[j][1])  # Use negative to simulate max-heap
                j += 1

            # Each previously active query reduces nums[i] by 1
            nums[i] -= len(min_heap)

            # Try using new queries (from max-heap) if nums[i] > 0 and they can cover index i
            while nums[i] > 0 and max_heap and -max_heap[0] >= i:
                ending = -heapq.heappop(max_heap)     # Get the farthest-ending query
                heapq.heappush(min_heap, ending)      # Add to active queries
                usedQueries += 1
                nums[i] -= 1

            # If we still have leftover work and no queries can help, return -1
            if nums[i] > 0:
                return -1

            # Remove expired queries from active heap
            while min_heap and min_heap[0] <= i:
                heapq.heappop(min_heap)

        # Return how many queries are left unused
        return q - usedQueries
