# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from sortedcontainers import SortedSet
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        st = SortedSet()  # To store unique valid 3-digit even numbers in sorted order

        # Try all possible combinations of 3 different digits
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # Skip if any two indices are the same (we need distinct positions)
                    if i == j or j == k or i == k:
                        continue

                    # Form the number from digits at i, j, k
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]

                    # Check if the number is a valid 3-digit even number
                    if num >= 100 and num % 2 == 0:
                        st.add(num)  # Automatically avoids duplicates

        return list(st)  # Convert sorted set to list before returning
