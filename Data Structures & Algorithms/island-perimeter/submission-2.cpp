class Solution {
public:
    int perim = 0;

    void dfs(int i, int j,
             vector<vector<int>>& grid,
             vector<vector<bool>>& visited) {

        if (i < 0 || j < 0 ||
            i >= grid.size() || j >= grid[0].size()) {
            perim++;
            return;
        }

        if (grid[i][j] == 0) {
            perim++;
            return;
        }

        if (visited[i][j]) {
            return;
        }

        visited[i][j] = true;

        dfs(i + 1, j, grid, visited);
        dfs(i - 1, j, grid, visited);
        dfs(i, j + 1, grid, visited);
        dfs(i, j - 1, grid, visited);
    }

    int islandPerimeter(vector<vector<int>>& grid) {
        vector<vector<bool>> visited(
            grid.size(),
            vector<bool>(grid[0].size(), false));

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1) {
                    dfs(i, j, grid, visited);
                    return perim;
                }
            }
        }

        return 0;
    }
};