class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_map = defaultdict(list)
        time_to_node = defaultdict(lambda: float("inf"))
        time_to_node[k] = 0

        for src, dst, time in times:
            adjacency_map[src].append((time, dst))

        heap = [(0, k)]
        visited = []

        while heap:
            time, node = heapq.heappop(heap)

            for neighbor_time, neighbor_node in adjacency_map[node]:
                if neighbor_time + time < time_to_node[neighbor_node]:
                    time_to_node[neighbor_node] = neighbor_time + time
                    heapq.heappush(heap, (time + neighbor_time, neighbor_node))

            visited.append(node)

        if len(time_to_node) == n:
            return max(time_to_node.values())
        else:
            return -1
