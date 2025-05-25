# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from collections import defaultdict
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mpp = defaultdict(int)  # Dictionary to count occurrences of words and their reverses
        ans = 0

        # Step 1: Try to pair words with their reverse
        for word in words:
            rev = word[::-1]  # Reverse the current word

            if mpp[rev] > 0:
                # Found a pair (e.g., "ab" + "ba" => palindrome of length 4)
                ans += 4
                mpp[rev] -= 1  # Decrease count of the reverse word
            else:
                # No pair found yet, store the word
                mpp[word] += 1

        # Step 2: Check for a word like "aa", "bb", etc. that can be in the middle
        for k, v in mpp.items():
            if k[0] == k[1] and v > 0:
                # We can place one of these symmetric words in the middle (adds 2 to palindrome length)
                ans += 2
                break  # Only one such word is needed

        return ans
