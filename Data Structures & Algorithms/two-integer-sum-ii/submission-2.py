class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            result = numbers[l] + numbers[r]
            
            if result == target:
                return [l + 1, r + 1]
            elif result > target:
                r = r - 1
            elif result < target:
                l = l + 1