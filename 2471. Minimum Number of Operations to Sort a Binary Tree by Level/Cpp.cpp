Approach : 

1 : Level-order Traversal (BFS):

a : Traverse the binary tree level by level.
b : For each level, collect the node values in a list (values).
c : Count Minimum Swaps to Sort Each Level:

2 : For each values list:
	
a : Create a sorted version of the list.
b : Use a hash map to track the indices of the original values.
c : Simulate sorting by swapping misplaced values into their correct positions, updating the hash map, and counting the swaps.

class Solution {
public:
    int countSwaps(vector<int>& values) {
        int swaps = 0;
        vector<int> sorted = values;
        sort(sorted.begin(), sorted.end());

        unordered_map<int, int> mp;
        for (int i = 0; i < values.size(); i++) {
            mp[values[i]] = i;
        }

        for (int i = 0; i < values.size(); i++) {
            if (values[i] != sorted[i]) {
                swaps++;
                int existingPos = mp[sorted[i]];
                mp[values[i]] = existingPos;
                mp[sorted[i]] = i;
                swap(values[existingPos], values[i]);
            }
        }
        return swaps;
    }

    int minimumOperations(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        int swaps = 0;

        while (!q.empty()) {
            int size = q.size();
            vector<int> values(size);

            for (int i = 0; i < size; i++) {
                TreeNode* cur = q.front();
                q.pop();
                values[i] = cur->val;

                if (cur->left) q.push(cur->left);
                if (cur->right) q.push(cur->right);
            }

            swaps += countSwaps(values);
        }
        return swaps;
    }
};
