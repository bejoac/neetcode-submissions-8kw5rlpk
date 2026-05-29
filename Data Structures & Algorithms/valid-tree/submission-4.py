class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjacency_map = defaultdict(list)

        for u, v in edges:
            adjacency_map[u].append(v)
            adjacency_map[v].append(u)

        visited = set([])
        stack = [(0, -1)]

        while stack:
            node, parent = stack.pop()

            if node in visited:
                return False

            for neighbor in adjacency_map[node]:
                if neighbor != parent:
                    stack.append((neighbor, node)) # node itselfs becomes parent
            
            visited.add(node)

        return len(visited) == n

        