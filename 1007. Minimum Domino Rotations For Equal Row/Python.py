# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    # Helper function to check how many swaps needed to make all values in tops or bottoms equal to `value`
    def find(self, tops, bottoms, value):
        swapTop, swapBottom = 0, 0  # Track number of swaps needed for tops and bottoms

        for i in range(len(tops)):
            # If neither top nor bottom has the target value, it's impossible to unify with this value
            if tops[i] != value and bottoms[i] != value:
                return -1
            
            # If top needs to be swapped to get the value
            elif tops[i] != value:
                swapTop += 1

            # If bottom needs to be swapped to get the value
            elif bottoms[i] != value:
                swapBottom += 1

        # Return the minimum number of swaps needed between top and bottom
        return min(swapTop, swapBottom)

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = float("inf")  # Initialize result with infinity

        # Try each possible value (1 to 6 for dominos)
        for value in range(1, 7):
            currentSwaps = self.find(tops, bottoms, value)
            # Update answer if the current value gives a valid swap count
            if currentSwaps != -1:
                ans = min(ans, currentSwaps)

        # If ans was updated from infinity, return it; otherwise, return -1 meaning not possible
        return ans if ans != float("inf") else -1
