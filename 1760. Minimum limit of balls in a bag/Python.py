# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

import math
from typing import List

class Solution:
    def isPossible(self, nums: List[int], maxOperations: int, l: int) -> bool:
        curr = 0  # Track the total operations required
        for b in nums:
            # Calculate how many splits are needed to ensure bag size <= l
            # Subtract 1 because no split is needed if b <= l
            curr += math.ceil(b / l) - 1
        # Check if the required operations are within the allowed limit
        return curr <= maxOperations

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Binary search range
        beg = 1  # Minimum possible size
        end = max(nums)  # Maximum size is the largest bag size
        res = end  # Initialize result to the maximum size

        while beg <= end:
            mid = (beg + end) // 2  # Middle value to check
            if self.isPossible(nums, maxOperations, mid):
                # If possible with mid as the maximum size, update result
                res = mid
                end = mid - 1  # Search for a smaller possible size
            else:
                beg = mid + 1  # Search for a larger possible size

        return res
