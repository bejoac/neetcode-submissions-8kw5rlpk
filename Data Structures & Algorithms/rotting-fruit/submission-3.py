class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        H, W = len(grid), len(grid[0])
        queue = deque()
        result = 0

        for i in range(H):
            for j in range(W):
                if grid[i][j] == 2:
                    queue.appendleft((i, j))

        while queue:
            i, j = queue.pop()

            for dh, dw in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = i + dh, j + dw

                if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == 1:
                    grid[ni][nj] = grid[i][j] + 1
                    result = max(result, grid[ni][nj] - 2)
                    queue.appendleft((ni, nj))        

        for i in range(H):
            for j in range(W):
                if grid[i][j] == 1:
                    result = -1

        return result