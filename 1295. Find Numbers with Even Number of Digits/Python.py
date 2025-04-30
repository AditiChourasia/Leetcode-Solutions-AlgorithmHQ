# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for num in nums: # traversing through the nums
            if len(str(num)) % 2 == 0: # if the length of the number is even, then increment the answer
                ans += 1

        return ans # return the answer at the end