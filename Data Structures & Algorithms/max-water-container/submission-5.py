class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0

        l, r = 0, len(heights) - 1
        
        while l < r:
            volume = min(heights[l], heights[r]) * len(heights[l:r])
            max_volume = max(max_volume, volume)

            if heights[l] <= heights[r]:   
                l += 1
            else:
                r -= 1

        return max_volume