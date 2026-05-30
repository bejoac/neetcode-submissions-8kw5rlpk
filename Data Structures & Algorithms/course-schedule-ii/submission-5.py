class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)

        for course, prereq in prerequisites:
            adjacency_list[course].append(prereq)

        visited, cycle = set([]), set([])
        path = []

        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True # Double add verhindern
            
            cycle.add(node)

            for next_node in adjacency_list[node]:
                if not dfs(next_node):
                    return False

            cycle.remove(node)
            visited.add(node)
            path.append(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return [] 
        return path



