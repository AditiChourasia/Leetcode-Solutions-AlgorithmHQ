# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        mpp = defaultdict(int)  # Dictionary to store the last occurrence of each character

        # Step 1: Store the last index of each character in the string
        for i in range(n):
            mpp[s[i]] = i  # Update to the last occurrence of s[i]

        size, end = 0, -1  # `size` tracks the current partition size, `end` tracks the farthest index for the current partition
        ans = []  # Stores the sizes of partitions

        # Step 2: Iterate through the string to form partitions
        for i in range(n):
            size += 1  # Increase the partition size
            end = max(end, mpp[s[i]])  # Update the end of the partition to the farthest last occurrence of a character in the partition

            # Step 3: If we reach `end`, finalize the partition
            if i == end:  
                ans.append(size)  # Add partition size to the result
                size = 0  # Reset for the next partition

        return ans
 