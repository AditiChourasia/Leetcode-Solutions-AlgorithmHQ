# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)

        left, right = 0, 0

        count = 0
        miniK, maxiK = -1, -1

        for right in range(n):
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
                miniK, maxiK = -1, -1
                continue

            if nums[right] == minK:
                miniK = right

            if nums[right] == maxK:
                maxiK = right

            if miniK != -1 and maxiK != -1:
                count += max((min(miniK, maxiK) - left + 1), 0)
            
        return count