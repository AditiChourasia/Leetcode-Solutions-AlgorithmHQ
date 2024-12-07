# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = 0
        ans = 0

        for i in range(1, n + 1):
            if (s + 10) <= maxSum and i not in banned:
                s += i
                ans += 1
        return ans