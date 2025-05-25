# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)

        # Create a difference array with one extra space
        diff = [0] * (n + 1)

        # Apply each query as a range decrement using the difference array technique
        for l, r in queries:
            diff[l] -= 1               # Start decrementing from index l
            if r + 1 < len(diff):      
                diff[r + 1] += 1       # Cancel out decrement after index r

        # Convert the difference array to the actual value changes (prefix sum)
        for i in range(1, n):
            diff[i] += diff[i - 1]

        # Apply the changes to the original array and check if all values are <= 0
        for i in range(n):
            if nums[i] + diff[i] > 0:
                return False           # If any value is still greater than 0, return False

        return True                    # All values are zero or less => return True
