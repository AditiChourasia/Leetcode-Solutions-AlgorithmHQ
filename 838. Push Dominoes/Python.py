# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        leftClosestR = [-1] * n  # Stores index of the nearest 'R' to the left
        rightClosestL = [-1] * n  # Stores index of the nearest 'L' to the right
        result = ['.'] * n  # Final result array initialized with '.'

        # Find the index of the closest 'R' on the left for each position
        lastR = -1
        for i in range(n):
            if dominoes[i] == 'R':
                lastR = i  # Update the last seen 'R'
            elif dominoes[i] == 'L':
                lastR = -1  # Reset if 'L' is encountered
            leftClosestR[i] = lastR

        # Find the index of the closest 'L' on the right for each position
        lastL = -1
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                lastL = i  # Update the last seen 'L'
            elif dominoes[i] == 'R':
                lastL = -1  # Reset if 'R' is encountered
            rightClosestL[i] = lastL

        # Determine final state for each domino
        for i in range(n):
            if dominoes[i] != '.':
                result[i] = dominoes[i]  # Keep 'L' or 'R' as it is
            else:
                left = leftClosestR[i]
                right = rightClosestL[i]

                distLeft = float('inf') if left == -1 else i - left
                distRight = float('inf') if right == -1 else right - i

                if distLeft == distRight:
                    result[i] = '.'  # Equal distance to both forces, remains upright
                elif distLeft < distRight:
                    result[i] = 'R'  # Closer to a 'R' force
                else:
                    result[i] = 'L'  # Closer to a 'L' force

        return "".join(result)
