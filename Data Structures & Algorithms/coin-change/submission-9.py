class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining: int) -> int:
            if remaining == 0:
                return 0

            if remaining in memo:
                return memo[remaining]

            res = 1e9

            for coin in coins:
                if remaining - coin >= 0:
                    res = min(res, 1 + dfs(remaining - coin))

            memo[remaining] = res
            return res

        res = dfs(amount)
        if res == 1e9:
            return -1
        return res