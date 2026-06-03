class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(cur: int) -> int:
            if cur == n:
                return 1

            if cur in memo:
                return memo[cur]

            if cur > n:
                return 0

            res = dfs(cur + 1) + dfs(cur + 2)
            memo[cur] = res
            
            return res
            
        return dfs(0)
