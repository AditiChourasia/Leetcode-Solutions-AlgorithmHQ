contributed by : Sundaram Agnihotri (student)
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach :

1 : A champion team a is a node with no incoming edges (in-degree = 0) and has a directed path to every other node in the DAG (is the only "source" node).

2 : Calculate the in-degree of each node using the given edges.
A node with in-degree 0 is a potential champion as no other node is stronger than it.

3 : Count the number of nodes with in-degree 0 , If there’s more than one source, return-1 (no unique champion).


class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<int> indegree(n);
        for(auto& edge: edges)
            indegree[edge[1]]++;
        
        int start_point=0;
        int champion;
        for(int i=0;i<n;++i)
            if(indegree[i]==0){
                start_point++;
                champion=i;
            }
        
        return start_point==1?champion:-1;
    }
};
