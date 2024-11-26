Contributed by : Sundaram (student)
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 
1 : To solve this problem efficiently, we can use Breadth-First Search (BFS). The BFS algorithm is suitable for 
finding the shortest path or minimum steps in problems like these because it explores all possible states level by level.
2 : Treat the 2x3 board as a one-dimensional string to simplify state representation. For example, the board [[1,2,3],[4,0,5]] can be represented as "123405".
The goal state is "123450".
3 : Since 0 represents the empty space, identify all possible swaps for each position based on the adjacency of cells in the 2x3 grid
4 : Start from the initial board state and use a queue to manage states to explore.
   For each state, generate all possible new states by swapping 0 with adjacent numbers.
   Keep track of visited states to avoid redundant computations.
   If the goal state is reached, return the number of moves taken to reach it.
   If the queue is exhausted without reaching the goal, return -1.
   
   
class Solution {
public:
    string helper(string str, int i, int j) {
        swap(str[i], str[j]);
        return str;
    }

    int slidingPuzzle(vector<vector<int>>& board) {
        vector<vector<int>> directions = {{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}};
        string target = "123450";
        string startState;
        
        for (const auto& row : board)
            for (int num : row)
                startState += to_string(num);

        unordered_set<string> visited;
        queue<string> queue;
        queue.push(startState);
        visited.insert(startState);

        int moves = 0;
        while (!queue.empty()) {
            int size = queue.size();
            while (size-- > 0) {
                string current = queue.front();
                queue.pop();
                if (current == target) return moves;

                int zeroPos = current.find('0');
                for (int newZeroPos : directions[zeroPos]) {
                    string nextState = helper(current, zeroPos, newZeroPos);
                    if (visited.count(nextState)) continue;
                    visited.insert(nextState);
                    queue.push(nextState);
                }
            }
            moves++;
        }
        return -1;
    }
};
