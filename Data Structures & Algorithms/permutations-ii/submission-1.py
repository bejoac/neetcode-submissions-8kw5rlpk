class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = set()
        perm = []
        perms = []

        def dfs(i):
            if len(perm) == len(nums) and perm not in perms:
                perms.append(perm.copy())
                return
            
            for j in range(len(nums)):
                if j in used:
                    continue
                
                perm.append(nums[j])
                used.add(j)
                dfs(j + 1)
                perm.pop()
                used.remove(j)

        dfs(0)
        return perms
