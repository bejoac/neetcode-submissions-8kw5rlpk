class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]


        while nums[-1] < nums[0]:
            r = nums.pop()
            nums.insert(0, r)

        return nums[0]