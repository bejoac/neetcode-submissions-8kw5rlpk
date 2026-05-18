class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(stair):
            if stair in memo:
                return memo[stair]

            if stair == n:
                return 1
            if stair > n:
                return 0

            stair_res = dfs(stair + 1) + dfs(stair + 2)
            memo[stair] = stair_res
            return stair_res

        return dfs(0) 