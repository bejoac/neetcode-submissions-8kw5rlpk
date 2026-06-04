class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)

        def dfs(i):
            if i == len(nums) - 1:
                return 

            dfs(i + 1)

            for j in range(i, len(memo)):
                if nums[i] < nums[j]:
                    memo[i] = max(memo[i], 1 + memo[j]) 

        dfs(0)
        return max(memo)