class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = []
        last_index = len(nums) - 1

        for i in range(0, len(nums)):
            for e in range(i + 1, len(nums)):
                if nums[i] + nums[e] == target:
                    indices.append(i)
                    indices.append(e)

        return indices

            
        