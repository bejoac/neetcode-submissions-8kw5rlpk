class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False

        half = total // 2
        memo = {}

        def dfs(i, cursum):
            if cursum == half:
                return True
            if i >= len(nums) or cursum > half:
                return False
            if (i, cursum) in memo:
                return memo[(i, cursum)]

            res = dfs(i + 1, cursum + nums[i]) or dfs(i + 1, cursum)
            memo[(i, cursum)] = res
            return res

        return dfs(0, 0)