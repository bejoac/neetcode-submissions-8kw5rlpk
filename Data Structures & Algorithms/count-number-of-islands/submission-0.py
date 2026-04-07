class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    h = len(grid) 
    w = len(grid[0])
    result = 0

    def bfs(row, col):
      q = deque()
      grid[row][col] = '0'
      q.append((row, col))

      while q:
        row, col = q.popleft()
        for dh, dw in directions:
          nrow, ncol = row + dh, col + dw
          if (nrow < 0 or ncol < 0 or nrow >= h or ncol >= w or grid[nrow][ncol] == '0'):
            continue
          q.append((nrow, ncol))
          grid[nrow][ncol] = '0'

    for row in range(0, h):
      for col in range(0, w):
        if grid[row][col] == '1':
          bfs(row=row, col=col)
          result = result + 1

    return result