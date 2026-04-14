class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        TOP = len(cost)
        memo = {}

        def dfs(i):
            if i >= TOP:
                return 0
            if i in memo:
                return memo[i]
            
            result = cost[i] + min(dfs(i + 1), dfs(i + 2))
            memo[i] = result
            return result
    
        return min(dfs(0), dfs(1))      