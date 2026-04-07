class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, 1

        nums = sorted(nums)

        if 0 not in nums:
            return 0

        while r <= len(nums) - 1:
            if nums[r] - nums[l] != 1:
                return nums[l] + 1

            l = l + 1
            r = r + 1
        
        return nums[r-1] + 1