class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)

        for i in range(len(nums) - 1, -1, -1):
            res = nums[i]
            allowed_values = [v for k, v in memo.items() if k > i + 1]
            if allowed_values:
                res += max(allowed_values)
            memo[i] = max(memo[i], res)

        return max(memo.values())