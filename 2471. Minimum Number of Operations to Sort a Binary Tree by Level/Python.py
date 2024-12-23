# Contributed by Pratham Chelaramani (Student)
# LinkedIn : https://www.linkedin.com/in/thepratholic/


from collections import deque, defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Helper function to calculate the minimum swaps required to sort an array
    def minSwap(self, arr):
        n = len(arr)  # Length of the array
        res = 0  # Counter for the number of swaps
        oldarr = arr[:]  # Create a copy of the array to store original values
        h = {}  # Dictionary to map values to their indices in the original array
        
        # Sort the array to determine the target order
        oldarr.sort()
        
        # Create a mapping of each value in the original array to its index
        for i in range(n):
            h[arr[i]] = i
        
        # Iterate through the array and perform swaps to align it with the sorted version
        for i in range(n):
            if arr[i] != oldarr[i]:  # If the current element is not in its sorted position
                res += 1  # Increment swap counter
                init = arr[i]  # Store the current value
                
                # Perform the swap
                arr[i], arr[h[oldarr[i]]] = arr[h[oldarr[i]]], arr[i]
                
                # Update the index mapping after the swap
                h[init] = h[oldarr[i]]
                h[oldarr[i]] = i
        
        return res  # Return the total number of swaps
    
    # Main function to calculate the minimum operations to reorder a binary tree level-by-level
    def minimumOperations(self, root) -> int:
        q = deque([(root, 0)])  # Queue for level-order traversal (node, level)
        levels = defaultdict(list)  # Dictionary to store node values at each level
        
        # Perform level-order traversal to group values by level
        while len(q) > 0:
            curr, l = q.pop()  # Get the current node and its level
            if curr:  # If the node is not null
                levels[l].append(curr.val)  # Append the node's value to its level
                q.appendleft((curr.left, l + 1))  # Add the left child to the queue
                q.appendleft((curr.right, l + 1))  # Add the right child to the queue
        
        res = 0  # Initialize the result (total operations)
        
        # Process each level to calculate the number of swaps needed to sort it
        for l in levels:
            res += self.minSwap(levels[l])  # Add the swaps required for the current level
        
        return res  # Return the total minimum operations