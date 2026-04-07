class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t = sorted(t)
        s = sorted(s)
        
        if t == s:
            return True
        else:
            return False