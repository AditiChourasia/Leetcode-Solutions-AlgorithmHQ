# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        ans = []              # To store the result subsequence
        f = groups[0]         # Initialize with the first group
        ans.append(words[0])  # Always include the first word

        # Loop through the remaining words
        for i in range(1, n):
            # If the current group is different from the previous, include the word
            if groups[i] != f:
                ans.append(words[i])
                f = groups[i]  # Update the group tracker

        return ans
