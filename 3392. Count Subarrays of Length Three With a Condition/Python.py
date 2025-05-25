# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n - 2):
            if 2 * (nums[i] + nums[i + 2]) == nums[i + 1]: # check wheather the middle element is half of the sum of first and third elements
                ans += 1

        return ans