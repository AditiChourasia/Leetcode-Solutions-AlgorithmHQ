# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0  # Two pointers: left and right of window
        sum, size = 0, 0  # sum = sum of current window, size = size of window

        cnt = 0  # Final count of valid subarrays

        while r < n:
            sum += nums[r]  # Add current element to window sum
            size += 1  # Increase window size

            # Shrink window from the left while condition is violated
            while l <= r and sum * size >= k:
                sum -= nums[l]  # Remove element at left
                size -= 1  # Decrease window size
                l += 1  # Move left pointer forward

            # After adjustments, all subarrays ending at r and starting from [l..r] are valid
            cnt += (r - l + 1)

            r += 1  # Move right pointer forward by one

        return cnt
