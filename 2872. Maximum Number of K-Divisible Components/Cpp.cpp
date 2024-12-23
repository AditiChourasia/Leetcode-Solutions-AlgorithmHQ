Contributed by : Sundaram Agnihotri
linkedin  : https://www.linkedin.com/in/sundaram-agnihotri/

Approach 

1 : Graph Representation:
Represent the tree as an adjacency list, gr, for efficient traversal. Store the degree of each node in inDegree.

2 : Leaf Node Identification:
Identify all leaf nodes (nodes with a degree of 1) and push them into a queue for processing.

3 : Bottom-Up Tree Traversal:
Perform a bottom-up traversal of the tree using a queue:

4 : Process leaf nodes and propagate their values to their neighbors.
Reduce the in-degree of the current node's neighbors.
Add a neighbor to the queue if its in-degree becomes 1 (making it the next leaf).
Component Count:
During the traversal:

If the value of a node modulo ?? k is 0, it forms a valid component. Increment the componentCount.
Propagate the remainder of the node's value (if not divisible by ?? k) to its parent.

Final Count:
By the end of the traversal, the componentCount will store the maximum number of components with values divisible by ?? k.

class Solution {
public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        if (n < 2) return 1;

        vector<vector<int>> gr(n);
        vector<int> inDegree(n);
        vector<long long> nodeValues(values.begin(), values.end());

        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            gr[u].push_back(v);
            gr[v].push_back(u);
            inDegree[u]++;
            inDegree[v]++;
        }

        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (inDegree[i] == 1) q.push(i);
        }

        int componentCount = 0;
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            inDegree[cur]--;
            long long addValue = (nodeValues[cur] % k == 0) ? 0 : nodeValues[cur];
            if (addValue == 0) componentCount++;

            for (int neighbor : gr[cur]) {
                if (inDegree[neighbor] > 0) {
                    inDegree[neighbor]--;
                    nodeValues[neighbor] += addValue;
                    if (inDegree[neighbor] == 1) q.push(neighbor);
                }
            }
        }

        return componentCount;
    }
};
