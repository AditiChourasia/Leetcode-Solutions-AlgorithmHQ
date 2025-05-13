# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        group = defaultdict(int)  # Keeps track of how many numbers fall into each digit sum group

        # Step 1: Count how many numbers have each digit sum
        for number in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(number))  # Calculate digit sum
            group[digit_sum] += 1  # Add to that digit sum group

        # Step 2: Find the maximum size among all groups
        maxi = max(group.values())

        # Step 3: Count how many groups have that maximum size
        return sum(1 for size in group.values() if size == maxi)
