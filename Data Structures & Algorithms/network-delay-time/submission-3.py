class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_map = defaultdict(list)
        time_to_node = defaultdict(lambda: float("inf"))


        for src, dst, time in times:
            adjacency_map[src].append((dst, time))

        queue = deque([(k, 0)])
        time_to_node[k] = 0

        while queue:
            node, curr_time = queue.popleft()

            for dst, time in adjacency_map[node]:
                new_time = curr_time + time
                if new_time < time_to_node[dst]:
                    time_to_node[dst] = new_time
                    queue.append((dst, new_time))
            
        if len(time_to_node) == n:
            return max(time_to_node.values())
        else:
            return -1