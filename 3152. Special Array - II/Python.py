# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        ans = []  # Result array to store boolean results for each query
        n = len(nums)

        # Step 1: Calculate parity differences for adjacent pairs
        # 1 if adjacent numbers have different parity, 0 otherwise
        parity_diff = [0] * (n - 1)
        for i in range(n - 1):
            parity_diff[i] = (nums[i] % 2) != (nums[i + 1] % 2)

        # Step 2: Build a prefix sum array for parity differences
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + parity_diff[i - 1]

        # Step 3: Process each query
        for s, e in queries:
            # Check the sum of parity differences in range [s, e - 1]
            # If the sum equals the number of pairs, all pairs have different parity
            if prefix_sum[e] - prefix_sum[s] == (e - s):  # e - s is the number of pairs
                ans.append(True)
            else:
                ans.append(False)

        return ans
