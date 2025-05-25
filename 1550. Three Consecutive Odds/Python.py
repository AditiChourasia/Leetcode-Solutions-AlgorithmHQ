# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n - 2):
            if arr[i] & 1 and arr[i+1] & 1 and arr[i + 2] & 1:
                return True

        return False