class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for num in nums.copy():
            if num == val:
                nums.remove(num)

        return len(nums)