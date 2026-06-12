class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        subset = []
        subsets = []

        counts = Counter(nums)

        def dfs():
            if len(subset) == len(nums):
                subsets.append(subset.copy())
                return

            for num in counts.keys():
                if not counts[num]:
                    continue

                subset.append(num)
                counts[num] -= 1

                dfs()

                subset.pop()
                counts[num] += 1

            return

        dfs()
        return subsets