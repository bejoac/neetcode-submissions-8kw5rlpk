class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        for i in range(len(nums)):
            if i - 1 < 0:
                left = 0
            else:
                left = nums[i - 1]
    
            right = nums[-1] - nums[i]
            if left == right:
                return i

        return -1