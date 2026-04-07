class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = {}
        
        for num in nums:
            if num in num_count.keys():
                return True

            else: 
                num_count[num] = 1
        
        return False


