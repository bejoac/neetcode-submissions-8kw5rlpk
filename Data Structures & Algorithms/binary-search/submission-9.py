class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        middle = len(nums) // 2

        while r >= l:
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                r = middle - 1
                middle = l + (r - l) // 2
            elif target > nums[middle]:
                l = middle + 1
                middle = l + (r - l) // 2

        return -1