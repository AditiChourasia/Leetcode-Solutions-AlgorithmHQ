# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        v = [0] * 100  # Array to count occurrences of each unique domino representation
        res = 0  # To store the result (number of equivalent domino pairs)

        for a, b in dominoes:
            # Normalize the domino so (a, b) and (b, a) are considered the same
            if a > b:
                a, b = b, a

            num = (a * 10) + b  # Encode the pair uniquely as a two-digit number

            res += v[num]  # Add the number of previously seen equivalent dominoes
            v[num] += 1  # Increment the count for this normalized domino

        return res  # Return total number of equivalent domino pairs
