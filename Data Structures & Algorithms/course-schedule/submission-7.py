class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        adjacency_list = defaultdict(list)

        for course, requirement in prerequisites:
            if course == requirement:
                return False
            adjacency_list[course].append(requirement)
   
        visited = set([])

        def dfs(node):
            if node in visited:
                return False

            visited.add(node)

            for requirement in adjacency_list[node]:
                if not dfs(requirement):
                    return False
                
            visited.remove(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
        
        

