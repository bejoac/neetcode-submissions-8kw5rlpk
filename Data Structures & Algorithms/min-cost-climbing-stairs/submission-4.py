class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        TOP = len(cost)
        memo = {}

        def dfs(curr_floor):
            if curr_floor >= TOP:
                return 0
            
            if curr_floor in memo:
                return memo[curr_floor]
            
            result = cost[curr_floor] + min(dfs(curr_floor + 1), dfs(curr_floor + 2))
            memo[curr_floor] = result
            return result
    
        return min(dfs(0), dfs(1))      