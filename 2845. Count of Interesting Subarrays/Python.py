# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res = 0  # Result: Number of interesting subarrays
        mpp = defaultdict(int)  # Stores frequency of prefix mod values
        mpp[0] = 1  # Base case: prefix mod 0 seen once (empty prefix)

        cur_cnt = 0  # Count of elements seen so far where element % modulo == k

        for element in nums:
            # If current element satisfies the condition, increment the count
            if element % modulo == k:
                cur_cnt += 1

            # Find what the count was at some earlier point so that:
            # (cur_cnt - previous_count) % modulo == k
            target = (cur_cnt - k) % modulo

            # Add the number of such previous prefixes to the result
            res += mpp[target]

            # Update the frequency map with current prefix mod value
            mpp[cur_cnt % modulo] += 1

        return res
