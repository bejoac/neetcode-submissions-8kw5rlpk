class Solution:
    def trap(self, heights: List[int]) -> int:
        
        res = 0

        max_left = []
        max_right = []

        for p in range(0, len(heights) + 1):
            if p == 0:
                max_left.append(0)
                continue

            if p == len(heights):
                max_right.append(0)
                continue

            max_left.append(max(heights[:p+1]))
            max_right.append(max(heights[p:]))

        for i in range(0, len(heights)):
            res = res + max(0, min(max_left[i], max_right[i]) - heights[i])

        return res