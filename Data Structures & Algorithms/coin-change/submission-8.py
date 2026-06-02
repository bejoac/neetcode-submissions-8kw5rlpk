class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining):
            if remaining == 0:
                return 0

            if remaining in memo:
                return memo[remaining]

            res = 1e9

            for c in coins:
                if remaining - c >= 0:
                    res = min(res, 1 + dfs(remaining - c))

            memo[remaining] = res
            return res

        min_coins = dfs(amount)
        if min_coins == 1e9:
            return -1
        else:
            return min_coins            