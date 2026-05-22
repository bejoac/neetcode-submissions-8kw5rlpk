class Solution:
    def jump(self, nums: List[int]) -> int:
        top = len(nums) - 1
        memo = {}

        def dfs(i):
            if i == top:
                return 0
            if i in memo:
                return 1 + memo[i]

            res = 1001

            for j in range(1, nums[i] + 1):
                if i + j > top:
                    break
                subres = dfs(i + j)
                res = min(res, subres)
                
            memo[i] = res
            return 1 + res

        return dfs(0)

