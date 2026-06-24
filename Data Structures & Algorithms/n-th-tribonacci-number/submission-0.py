class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}
        
        if n < 3:
            return memo[n]

        for i in range(n + 1):
            if i < 3:
                result = memo[i]
            else:
                result = memo[i-1] + memo[i-2] + memo[i-3]
                memo[i] = result

        return memo[n]