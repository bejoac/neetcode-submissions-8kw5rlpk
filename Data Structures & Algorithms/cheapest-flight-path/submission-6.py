class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacency_list = defaultdict(list)

        for flight in flights:
            adjacency_list[flight[0]].append(flight[1:])

        min_heap = [(0, 0, src)] 
        heapq.heapify(min_heap)
        visited = defaultdict(int)

        min_cost = float('inf')

        while min_heap:
            curr_cost, stops, node = heapq.heappop(min_heap)
            
            if node == dst:
                min_cost = min(min_cost, curr_cost)
                break
            if stops > k:
                continue
            if node in visited and visited[node] <= stops:
                continue
            
            visited[node] = stops
            
            for next_node, cost in adjacency_list[node]:
                heapq.heappush(min_heap, (curr_cost + cost, stops + 1, next_node))

        if min_cost == float('inf'):
            return -1
        else:
            return min_cost