# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        mpp = defaultdict(int)  # To store frequency of elements in current window
        total = len(set(nums))  # Total distinct elements in the whole array
        inside = 0              # Distinct elements in current window

        ans, l, r = 0, 0, 0     # Pointers and result

        while l < n:
            # Move right pointer until all distinct elements are included in window
            while r < n and inside < total:
                if mpp[nums[r]] == 0:
                    inside += 1
                mpp[nums[r]] += 1
                r += 1

            # If the current window contains all distinct elements
            if inside == total:
                ans += (n - r + 1)  # All subarrays starting from l and ending at r...n-1 are valid

            # Move left pointer to shrink the window
            mpp[nums[l]] -= 1
            if mpp[nums[l]] == 0:
                inside -= 1

            l += 1 

        return ans
