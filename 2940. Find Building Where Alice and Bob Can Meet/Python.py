# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/thepratholic/

from typing import List
from collections import defaultdict

class SparseTable:
    # Constructor: Initializes the sparse table for range queries
    def __init__(self, arr, func, init):
        self.func = func  # Function to perform range operations (e.g., max or min)
        self.init = init  # Default value for unused table cells (e.g., float('-inf') for max queries)
        n = len(arr)  # Size of the input array
        k = n.bit_length()  # Maximum number of levels in the table (log2(n))
        
        # Initialize the table with the default value
        table = [[self.init] * k for _ in range(n)]
        
        # Precompute powers of 2 for quick interval calculations
        self.mpow = [(0, 1)] * (n + 1)
        l = 0  # Current power level
        p = 1  # Current power value (2^l)
        for i in range(1, n + 1):
            if p * 2 <= i:  # When to increment the power level
                l += 1
                p *= 2
            self.mpow[i] = (l, p)  # Store the power level and value for each position
        
        # Build the sparse table
        for l in range(k):  # Iterate through levels
            for i in range(n):  # Iterate through array elements
                if l == 0:  # Base level: directly take array values
                    table[i][l] = arr[i]
                else:  # Higher levels: combine results of smaller intervals
                    a = table[i][l - 1]  # Left interval
                    b = self.init  # Default for right interval if it goes out of bounds
                    if i + (1 << (l - 1)) < n:  # Ensure right interval is valid
                        b = table[i + (1 << (l - 1))][l - 1]
                    table[i][l] = self.func(a, b)  # Compute using the function (e.g., max)
        
        self.table = table  # Store the constructed table

    # Query function: Answers range queries using the sparse table
    def query(self, l, r):
        i, p = self.mpow[r - l + 1]  # Get the largest power-of-2 interval covering the range
        # Combine the results of the two intervals
        return self.func(self.table[l][i], self.table[r - p + 1][i])

class Solution:
    # Main function to process the queries
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)  # Number of buildings
        res = []  # Result array to store answers to each query
        
        # Initialize the sparse table with heights array and max function
        sp = SparseTable(heights, lambda x, y: max(x, y), float('-inf'))
        
        # Process each query
        for a, b in queries:
            a, b = min(a, b), max(a, b)  # Ensure a is always less than or equal to b
            
            # Case 1: If both indices are the same, the answer is the index itself
            if a == b:
                res.append(a)
                continue

            # Case 2: If building `b` is already taller than building `a`, return `b`
            if heights[b] > heights[a]:
                res.append(b)
                continue

            # Case 3: Use binary search with the sparse table to find the next taller building
            val = max(heights[a], heights[b])  # Determine the height threshold
            pos = b  # Start binary search from position `b`
            beg = b + 1  # Binary search lower bound
            end = n - 1  # Binary search upper bound
            curr = n  # Default: No valid building found

            # Perform binary search
            while beg <= end:
                mid = (beg + end) // 2  # Middle of the search range
                # Query the sparse table for the maximum height in the range [pos, mid]
                if sp.query(pos, mid) > val:
                    curr = mid  # Update current result
                    end = mid - 1  # Narrow search to the left
                else:
                    beg = mid + 1  # Narrow search to the right

            # Append the result: Either the found building or -1 if none exists
            if curr < n:
                res.append(curr)
            else:
                res.append(-1)

        return res  # Return the results for all queries
