class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(nums)

        max_count = 1
        res = 1

        cur_i, next_i = 0, 1

        while next_i < len(nums):
            if abs(nums[next_i] - nums[cur_i]) == 1:
                res = res + 1
                max_count = max(max_count, res)
            elif nums[next_i] - nums[cur_i] == 0:
                cur_i += 1
                next_i += 1
                continue
            else:
                res = 1

            cur_i += 1
            next_i += 1

        return max_count