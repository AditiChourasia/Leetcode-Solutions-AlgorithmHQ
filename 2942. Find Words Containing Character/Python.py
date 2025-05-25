# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/pratham-chelaramani-a44283227/


from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)

        ans = [] # result list

        for i in range(n):
            word = words[i]
            if x in word: # checking if the given x character is in the current word, if yes then add that word in the result list
                ans.append(i)


        return ans # return the answer list