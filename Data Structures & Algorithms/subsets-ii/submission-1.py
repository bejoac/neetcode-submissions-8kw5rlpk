class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                for sub in subsets:
                    if sorted(sub) == sorted(subset):
                        return
                subsets.append(subset.copy())
                return 
            
            subset.append(nums[i])
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)
            return
        
        dfs(0)
        return subsets