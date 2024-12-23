# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/thepratholic/

from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)  # Length of the array
        res = 0  # Initialize the chunk counter
        prev = -1  # Initialize the previous chunk boundary

        # Iterate through each element in the array
        for i in range(n):
            j = n - 1  # Start from the end of the array
            # Find the farthest index 'j' where arr[j] >= arr[i]
            while j > i and arr[j] >= arr[i]:
                j -= 1
            
            # If the current index 'i' is greater than the last chunk boundary, start a new chunk
            if i > prev:
                res += 1  # Increment the chunk counter

            # Update the last chunk boundary to extend the current chunk
            prev = max(prev, j)

        return res  # Return the total number of chunks
