# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_element = max(nums)  # Find the maximum element in nums
        l, r = 0, 0  # Initialize left and right pointers
        count_of_maximum = 0  # Counts how many max elements in current window
        ans = 0  # Final answer to store total subarrays

        while r < n:
            # If the current element is the maximum, increment count
            if nums[r] == max_element:
                count_of_maximum += 1

            # While we have exactly k max elements in window, shrink from left
            while count_of_maximum == k:
                # If the element at left was maximum, reduce its count
                if nums[l] == max_element:
                    count_of_maximum -= 1
                l += 1  # Move left pointer ahead

            # For current r, all subarrays ending at r and starting before l are valid
            ans += l

            # Move right pointer to expand the window
            r += 1

        return ans
