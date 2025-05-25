# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0  # Initialize a counter to keep track of symmetric numbers

        # Loop through every number from low to high (inclusive)
        for num in range(low, high + 1):
            s = str(num)  # Convert the number to a string to easily access digits
            n = len(s)    # Find the number of digits

            # If the number of digits is odd, it cannot be symmetric as per the condition
            if n % 2 == 1:
                continue  # Skip this number

            half = n // 2  # Find the halfway point of the digits

            # Calculate the sum of the first half and the second half digits
            left_sum = sum(int(d) for d in s[:half])
            right_sum = sum(int(d) for d in s[half:])

            # If both halves have the same sum, count it as a symmetric number
            if left_sum == right_sum:
                res += 1

        return res  # Return the total count of symmetric numbers
