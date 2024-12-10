# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)

        # Step 1: Create a mapping for start and end times
        mp = {}
        for a, b, c in events:
            mp[a] = mp[b] = 0  # Initialize mapping for all unique start and end times

        # Step 2: Assign sorted indices to unique start and end times
        for i, el in enumerate(sorted(mp)):
            mp[el] = i

        # Step 3: Sort events by start time
        events.sort()

        # Step 4: Precompute maximum values from the end of the timeline
        maxscore = [0] * (len(mp) + 1)  # Stores max values for each point in time
        j = n - 1  # Pointer for events
        maxyet = 0  # Track the maximum value encountered so far

        # Iterate backward to calculate maximum values
        for i in range(len(mp), -1, -1):
            while j >= 0 and mp[events[j][0]] >= i:
                # Update the maximum value up to this point
                maxyet = max(maxyet, events[j][2])
                j -= 1
            maxscore[i] = maxyet

        # Step 5: Calculate the result using the precomputed maximums
        res = 0
        for a, b, c in events:
            # Max value is the current event's value + best value after the event's end
            res = max(res, c + maxscore[mp[b] + 1])

        return res
