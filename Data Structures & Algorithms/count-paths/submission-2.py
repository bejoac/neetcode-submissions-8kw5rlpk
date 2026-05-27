class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[-1] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0

            if grid[i][j] != -1:
                return grid[i][j]

            if i == m - 1 and j == n - 1:
                return 1


            grid[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return grid[i][j]
    
        return dfs(0, 0)