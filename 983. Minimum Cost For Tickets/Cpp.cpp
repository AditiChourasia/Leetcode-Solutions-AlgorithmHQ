contributed by : Sundaram Agnihotri
linkedin : https://www.linkedin.com/in/sundaram-agnihotri/

Approach : 

1 : Maintain two queues:
q1: Tracks the minimum cost for valid 7-day passes.
q2: Tracks the minimum cost for valid 30-day passes.
Remove expired entries for each day from these queues to ensure only valid passes are considered.

2 : Maintain two queues:
q1: Tracks the minimum cost for valid 7-day passes.
q2: Tracks the minimum cost for valid 30-day passes.
Remove expired entries for each day from these queues to ensure only valid passes are considered.

class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs,int cost =0) {
        queue<pair<int,int>>q1,q2;

        for(auto d : days){
            while(!q1.empty() && q1.front().first+7 <=d) q1.pop();
            while(!q2.empty() && q2.front().first+30 <=d) q2.pop();

            q1.push({d,cost + costs[1]});
            q2.push({d,cost + costs[2]});

            cost = min({cost+costs[0],q1.front().second,q2.front().second});
        }
        return cost;
    }
};
