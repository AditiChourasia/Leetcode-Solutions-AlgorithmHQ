# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        n = len(nums)

        if nums[0] == nums[1] == nums[2]: # if all the angles are same
            return "equilateral"

        elif (nums[0] == nums[1] and nums[0] + nums[1] > nums[2]) or (nums[0] == nums[2] and nums[0] + nums[2] > nums[1]) or (nums[1] == nums[2] and nums[1] + nums[2] > nums[0]):
            return "isosceles" # if any two angles are same

        elif nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
            return "scalene" # if any two sides have sum greater than third side

        else:
            return "none" # if none of the cases match , then return none