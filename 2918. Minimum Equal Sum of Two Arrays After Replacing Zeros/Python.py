# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Count the number of zeros in both lists
        z1 = nums1.count(0)
        z2 = nums2.count(0)

        # For each zero, assume we can replace it with minimum value 1
        # So we add the number of zeros to the sum
        sum_nums1 = sum(nums1) + z1
        sum_nums2 = sum(nums2) + z2

        # If nums1 sum is less and we cannot change anything in nums1 (no zeros), it's invalid
        if sum_nums1 < sum_nums2 and z1 == 0:
            return -1

        # Similarly, if nums2 sum is less and we cannot increase it (no zeros), it's invalid
        if sum_nums2 < sum_nums1 and z2 == 0:
            return -1

        # Return the maximum of the two updated sums
        return max(sum_nums1, sum_nums2)
