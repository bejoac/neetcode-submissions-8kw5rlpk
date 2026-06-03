class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)
        n = len(nums) - 1
        
        for i in range(n, -1, - 1):
            for j in range(i, n + 1):
                if nums[j] > nums[i]: 
                    memo[i] = max(memo[i], 1 + memo[j])
                    
        return max(memo)