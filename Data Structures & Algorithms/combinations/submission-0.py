class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n + 1)]

        subsets = []
        subset = []

        def dfs(i):
            if len(subset) == k:
                subsets.append(subset.copy())
                return

            if i >= n:
                return 

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return subsets
            
