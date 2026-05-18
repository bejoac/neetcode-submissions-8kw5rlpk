class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []
        candidates.sort()
        
        def dfs(i):
            if sum(combination) == target:
                combinations.append(combination.copy())
                return

            if i == len(candidates) or sum(combination) > target:
                return
            
            combination.append(candidates[i])
            dfs(i + 1)

            combination.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return combinations