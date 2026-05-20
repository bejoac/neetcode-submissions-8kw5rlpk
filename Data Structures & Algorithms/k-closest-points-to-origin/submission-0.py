class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        result = []

        for (x, y) in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (distance, [x, y]))

        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])

        return result