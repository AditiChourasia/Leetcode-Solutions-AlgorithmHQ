# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7  # Modulo to prevent overflow
        dp = {}  # Dictionary for memoization

        def helper(length):
            # Base case: If the length exceeds the high limit, stop recursion
            if length > high:
                return 0

            # If the result for the current length is already computed, return it
            if length in dp:
                return dp[length]

            # Initialize the count for the current length
            # Add 1 if the current length is within the valid range [low, high]
            dp[length] = 1 if length >= low else 0

            # Add contributions from appending 'zero' and 'one'
            dp[length] += helper(length + zero) + helper(length + one)

            # Return the result modulo `mod` to ensure it doesn't overflow
            return dp[length] % mod

        # Start the recursion from length 0
        return helper(0)
