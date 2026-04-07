class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0

        for r in range(len(heights) -1, 0, -1):
            l = 0
            while l < r:
                volume = min(heights[l], heights[r]) * len(heights[l:r])
                max_volume = max(max_volume, volume)
                
                l += 1


        return max_volume