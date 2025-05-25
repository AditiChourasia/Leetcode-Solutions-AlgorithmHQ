# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        min_prefix = 0  # Minimum prefix sum so far
        max_prefix = 0  # Maximum prefix sum so far

        # Calculate prefix sum and track its min and max
        for diff in differences:
            prefix += diff
            min_prefix = min(min_prefix, prefix)
            max_prefix = max(max_prefix, prefix)

        # To ensure the array stays within bounds:
        # lower ≤ a[i] ≤ upper for all i
        # Let original[0] = x, then all others are x + some prefix
        # So: x + min_prefix ≥ lower → x ≥ lower - min_prefix
        #     x + max_prefix ≤ upper → x ≤ upper - max_prefix
        lower_bound = lower - min_prefix
        upper_bound = upper - max_prefix

        # Count all possible values for original[0]
        return max(0, upper_bound - lower_bound + 1)
