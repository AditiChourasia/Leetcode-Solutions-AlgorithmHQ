Contributed by : Sundaram Agnihotri
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 

1 : Initialization:

a : Initialize the result array ans with -1 for all queries since by default, Alice and Bob might not meet.
b : Use an unordered map mp to store deferred queries that need additional processing, indexed by the maximum of Alice's and Bob's building indices.
Initial Query Processing:

2 : For each query [ai, bi]:
	
a : If Alice can move directly to Bob's building (i.e., i < j and h[i] < h[j]), set ans to j.
b : If Bob can move directly to Alice's building (i.e., i > j and h[i] > h[j]), set ans to i.
c : If Alice and Bob are in the same building (i == j), set ans to i.
d : Otherwise, store the query in mp for later processing. The key is max(ai, bi), and the value is the pair [max(h[ai], h[bi]), query_index].

3 : Deferred Query Processing:

Use a priority queue pq (min-heap) to process deferred queries in ascending order of height.
Iterate through all buildings:
	
4 : For each building:
	
While the top of pq has a height less than the current building height, update the ans array for the query at pq.top().second to the current building index.
Add deferred queries from mp corresponding to the current building index to the pq.

Final Result:

Return the ans array after processing all queries.

class Solution {
public:
    vector<int> leftmostBuildingQueries(vector<int>& h, vector<vector<int>>& queries) {
        int n = h.size(), m = queries.size();
        vector<int> ans(m, -1);
        unordered_map<int, vector<pair<int, int>>> mp;
        
        for(int id=0;id<m;id++){
            auto query = queries[id];
            int i = query[0], j = query[1];
            if(i<j && h[i] < h[j]){
                ans[id] = j;
            }else if(i>j && h[i] > h[j]){
                ans[id] = i;
            }else if(i==j){
                ans[id] = i;
            }else{
                mp[max(i, j)].push_back({ max(h[i], h[j]) , id});
            }
        }
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for(int id=0;id<n;id++){
            int curh = h[id];
            while(!pq.empty() && pq.top().first < curh){
                ans[pq.top().second] = id;
                pq.pop();
            }
            
            for(auto p : mp[id]){
                pq.push(p);
            }
        }
        
        return ans;
    }
};
