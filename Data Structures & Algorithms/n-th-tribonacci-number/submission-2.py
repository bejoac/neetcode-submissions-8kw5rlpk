class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def dfs(i: int) -> int:
            if i in memo:
                return memo[i]

            if i == 0:
                return 0
            elif i <= 2:
                return 1

            result = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
            memo[i] = result
            
            return result

        return dfs(n)