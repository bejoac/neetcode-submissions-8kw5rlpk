class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []
        subsets = []
        xor_sum = 0

        def dfs(i):
            nonlocal xor_sum
            
            if i == len(nums):
                tmp = 0
                for num in subset:
                    tmp = tmp ^ num
                xor_sum = xor_sum + tmp
                return 

            subset.append(nums[i])
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return xor_sum
