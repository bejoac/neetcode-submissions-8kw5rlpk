class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() != n - 1) {
            return false;
        };
        
        unordered_map<int, vector<int>> adjacency_map;

        for (vector<int> edge : edges) {
            adjacency_map[edge[0]].push_back(edge[1]);
            adjacency_map[edge[1]].push_back(edge[0]);
        };
        
        set<int> visited;
        vector<pair<int, int>> stack = {{0, -1}}; // node, parent
        
        while (stack.size() > 0) {
            int node = stack.back().first;
            int parent = stack.back().second;
            stack.pop_back();
            
            if (visited.find(node) != visited.end()) {
                return false;
            };
            
            for (int v : adjacency_map[node]) {
                if (v != parent) {
                    stack.push_back({v, node});
                };
            };
            
            visited.insert(node);
        };
        
        return visited.size() == n;
    };
};
