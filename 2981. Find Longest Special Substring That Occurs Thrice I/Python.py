# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/thepratholic/

from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        lens = defaultdict(list)
        i = 0
        res = -1

        # Step 1: Populate the lens dictionary with sequence lengths
        while i < n:
            ctr = 1
            while i < n - 1 and s[i] == s[i + 1]:
                ctr += 1
                i += 1
            lens[s[i]].append(ctr)
            if ctr >= 3:
                res = max(res, ctr - 2)  # Directly consider sequences of length >= 3
            i += 1

        # Step 2: Process the lens dictionary for combined sequences
        for c in lens:
            counts = sorted(lens[c], reverse=True)  # Sort lengths in descending order
            if len(counts) >= 3:
                res = max(res, counts[2])  # Consider the third largest
            if len(counts) >= 2:
                res = max(res, counts[1] - 1)  # Consider the second largest reduced by 1

        return res if res != -1 else 0  # Ensure to return 0 if no valid sequence exists
