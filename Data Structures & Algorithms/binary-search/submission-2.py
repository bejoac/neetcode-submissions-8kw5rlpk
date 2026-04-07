class Solution:
    def search(self, nums: List[int], target: int) -> int:
        t_index = None
        helper = 0

        while not t_index:
            if len(nums) == 1 and nums[0] == target:
                return 0

            middle = len(nums) // 2

            if middle == 0:
                return -1

            if target == nums[middle]:
                if helper == 0:
                    t_index = middle
                elif helper != 0:
                    t_index = helper + middle
                return t_index

            if target > nums[middle]:
                nums = nums[middle:]
                helper += middle

            else:
                nums = nums[:middle]


 