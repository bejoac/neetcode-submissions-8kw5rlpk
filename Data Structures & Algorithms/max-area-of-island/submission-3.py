class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        H, W = len(grid), len(grid[0])

        def search(i ,j):
            if not 0 <= i < H or not 0 <= j < W:
                return 0

            if grid[i][j] == 0:
                return 0

            # visited
            grid[i][j] = 0

            return 1 + (search(i + 1, j) 
                    + search(i, j + 1)
                    + search(i - 1, j)
                    + search(i, j - 1))
        
        i, j = 0, 0
        count = 0

        for i in range(H):
            for j in range(W):
                if grid[i][j] == 0:
                    continue
                count = max(search(i, j), count)

        return count
