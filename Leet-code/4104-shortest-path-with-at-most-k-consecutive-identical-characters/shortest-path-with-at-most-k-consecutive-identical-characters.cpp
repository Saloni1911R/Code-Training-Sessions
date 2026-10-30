class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        // Step 1: Build the adjacency list
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back({edge[1], edge[2]});
        }
        
        // Step 2: Track min-distance using a 2D table
        // dist[u][count] stores the shortest distance to node 'u' 
        // arriving with 'count' consecutive identical characters.
        const int INF = 1e9 + 7;
        vector<vector<int>> dist(n, vector<int>(k + 1, INF));
        
        // Min-heap storing: {current_cost, current_node, consecutive_count}
        priority_queue<tuple<int, int, int>, 
                       vector<tuple<int, int, int>>, 
                       greater<tuple<int, int, int>>> pq;
        
        // Base case: Starting at node 0 has a cost of 0 and a run of 1 character
        dist[0][1] = 0;
        pq.push({0, 0, 1});
        
        while (!pq.empty()) {
            auto [cost, u, count] = pq.top();
            pq.pop();
            
            // If we reached the target node, this must be the minimal cost path
            if (u == n - 1) {
                return cost;
            }
            
            // Skip outdated states
            if (cost > dist[u][count]) continue;
            
            // Explore outgoing directed neighbors
            for (const auto& neighbor : adj[u]) {
                int v = neighbor.first;
                int weight = neighbor.second;
                
                // Determine the consecutive run length at the next node
                int next_count = (labels[u] == labels[v]) ? (count + 1) : 1;
                
                // Only proceed if we do not exceed the threshold limit 'k'
                if (next_count <= k) {
                    if (cost + weight < dist[v][next_count]) {
                        dist[v][next_count] = cost + weight;
                        pq.push({dist[v][next_count], v, next_count});
                    }
                }
            }
        }
        
        return -1;
    }
};
