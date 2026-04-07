import heapq

class Solution:
  def lastStoneWeight(self, stones: List[int]) -> int:
    if not stones:
      return 0
    
    while len(stones) > 1:

      x, y = heapq.nlargest(2, stones)

      if x == y:
        if len(stones) == 2:
          return 0
        stones.remove(x)
        stones.remove(y)

      if y < x:
        stones.remove(x)
        stones.remove(y)
        heapq.heappush(stones, x - y)

    return heapq.heappop(stones)