class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []

        for _ in range(m):
            row = [0] * n
            grid.append(row)

        grid[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    grid[i + 1][j] += grid[i][j] # go down
                if j + 1 < n:
                    grid[i][j + 1] += grid[i][j] # go right

        return grid[m-1][n-1]