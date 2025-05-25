# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        
        # Initialize pointers
        low, mid, high = 0, 0, n - 1

        # Traverse the list and sort it using Dutch National Flag algorithm
        while mid <= high:
            if nums[mid] == 0:
                # Swap current element with element at 'low' index
                nums[low], nums[mid] = nums[mid], nums[low]
                # Move both pointers ahead
                mid += 1
                low += 1

            elif nums[mid] == 1:
                # Just move mid if it's already 1
                mid += 1

            else:
                # nums[mid] == 2
                # Swap with the element at 'high' and decrease 'high'
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
                # Note: Do not increase mid here because the swapped element needs to be checked
