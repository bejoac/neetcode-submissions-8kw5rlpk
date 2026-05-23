class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}

        def dfs(i):
            if i == 0:
                return 1
            
            if i in memo:
                return memo[i]

            if i % 2 == 0:
                res = dfs(i // 2) * dfs(i // 2)
            else:
                res = dfs(i // 2) * dfs(i // 2) * x

            memo[i] = res
            return res
        
        powered = dfs(abs(n))

        if n < 0: 
            return 1 / powered
        else:
            return powered