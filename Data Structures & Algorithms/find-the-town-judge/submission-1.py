class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = defaultdict(int)
        outdegrees = defaultdict(int)

        for src, dst in trust:
            outdegrees[src] += 1
            indegrees[dst] += 1

        for i in range(1, n + 1):
            if indegrees[i] == n - 1 and outdegrees[i] == 0:
                return i

        return -1