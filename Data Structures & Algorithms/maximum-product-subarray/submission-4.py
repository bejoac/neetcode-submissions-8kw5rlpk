class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min, cur_max = 1, 1
        res = nums[0]

        for num in nums:
            tmp = num * cur_max
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(tmp, num * cur_min, num)
            res = max(res, cur_max)

        return res
