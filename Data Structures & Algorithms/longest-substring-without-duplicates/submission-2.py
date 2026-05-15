class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        res = 0
        sub_array = []

        for r in range(len(s)):
            while s[r] in sub_array:
                sub_array.remove(s[l])
                l = l + 1
            sub_array.append(s[r])
            res = max(res, len(sub_array))

        return res
