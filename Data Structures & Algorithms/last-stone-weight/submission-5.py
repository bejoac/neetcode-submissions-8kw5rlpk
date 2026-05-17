class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))

            if x == y:
                continue
            else:
                heapq.heappush(stones, -abs(x - y))
        
        if stones:
            return -stones[0]
        return 0