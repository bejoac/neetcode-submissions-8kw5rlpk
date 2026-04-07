from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combos = list(combinations(nums, 3))

        results = []

        for combo in combos:
            combo = sorted(list(combo))
            if sum(combo) == 0 and combo not in results:
                results.append(combo)

        return results