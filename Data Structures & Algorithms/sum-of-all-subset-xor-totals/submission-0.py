class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []
        subsets = []

        def dfs(i):
            if i == len(nums):
                subsets.append(subset.copy())
                return 

            subset.append(nums[i])
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)

        dfs(0)

        xor_sum = 0

        for subset in subsets: 
            xor_sum_subset = 0
            for num in subset:
                xor_sum_subset = xor_sum_subset ^ num
            xor_sum = xor_sum + xor_sum_subset

        return xor_sum
