# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/thepratholic/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root):
        # Initialize a queue for BFS traversal
        q = deque([root])

        i = 0  # Level counter (0-based index)
        
        while q:
            # If the current level is odd, reverse the node values
            if i & 1:
                l, r = 0, len(q) - 1  # Two pointers for reversing values
                while l < r:
                    # Swap values at l and r indices
                    q[l].val, q[r].val = q[r].val, q[l].val
                    l += 1
                    r -= 1
            
            # Process the current level and enqueue the next level
            for _ in range(len(q)):
                node = q.popleft()
                # Add left and right children if they exist
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            
            # Increment the level counter
            i += 1
        
        return root  # Return the modified tree
