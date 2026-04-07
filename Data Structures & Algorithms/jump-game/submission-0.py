class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):
            # Base Case
            if i == len(nums) - 1:
                return True

            # Recursion Case
            end = min(len(nums) - 1, i + nums[i])

            for j in range(i + 1, end + 1):
                if dfs(j):
                    return True

            return False

        return dfs(0)       