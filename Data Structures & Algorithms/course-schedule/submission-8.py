class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses

        adjacency_map = defaultdict(list)

        for course, prereq in prerequisites:
            adjacency_map[prereq].append(course) # Arrow points from Prereq to Course
            indegrees[course] += 1

        queue = deque([])

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i) # i ~ course

        while queue:
            course = queue.popleft()

            for next_course in adjacency_map[course]:
                indegrees[next_course] -= 1 # Cause we finished given course
                
                if indegrees[next_course] == 0:
                    queue.appendleft(next_course)

        if sum(indegrees) != 0:
            return False

        return True