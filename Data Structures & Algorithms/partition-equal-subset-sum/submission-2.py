class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        half = total // 2

        def dfs(i, cursum):
            if cursum == half:
                return True

            if i >= len(nums):
                return False

            for j in range(i+1, len(nums)):
                if dfs(j, cursum + nums[j]):
                    return True
            return False

        return dfs(0, 0)