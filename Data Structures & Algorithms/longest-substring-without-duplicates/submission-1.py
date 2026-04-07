class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
            
        for r in range(1, len(s) + 1):
            l = 0
            while r <= len(s):
                if len(set(s[l:r])) == len(s[l:r]):
                    max_l = len(s[l:r])
                l+=1
                r+=1

        return max_l