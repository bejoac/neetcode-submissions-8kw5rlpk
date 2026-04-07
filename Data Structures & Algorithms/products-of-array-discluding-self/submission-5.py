class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        def calc_product(nums, i):
            intermediary_result = 1

            for num in nums:
                intermediary_result = intermediary_result * num

            result.append(intermediary_result)
        
        for i in range(0, len(nums)):
            nums_copy = nums.copy()
            nums_copy.pop(i)
            calc_product(nums_copy, i)
        

        return result