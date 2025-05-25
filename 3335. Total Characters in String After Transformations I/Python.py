# Contributed by Pratham Chelaramani (Student)
# LinkedIn: https://www.linkedin.com/in/pratham-chelaramani-a44283227/


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        mpp = [0] * 26
        for c in s:
            mpp[ord(c) - ord('a')] += 1

        for _ in range(t):
            temp = [0] * 26
            for i in range(26):
                f = mpp[i] % MOD

                if i != 25:
                    temp[(i + 1) % 26] = (temp[(i + 1) % 26] + f) % MOD
                
                else:
                    temp[0] = (temp[0] + f) % MOD
                    temp[1] = (temp[1] + f) % MOD

            mpp = temp

        return sum(mpp) % MOD