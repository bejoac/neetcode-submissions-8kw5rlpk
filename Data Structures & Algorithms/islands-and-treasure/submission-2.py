class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        queue = deque()
        H, W = len(grid), len(grid[0])
        
        # Find all zeroes
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 0:
                    queue.appendleft((i, j))

        while queue:
            i, j = queue.pop()

            for (dh, dw) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + dh, j + dw

                if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == INF:
                    grid[ni][nj] = grid[i][j] + 1
                    queue.appendleft((ni, nj))
