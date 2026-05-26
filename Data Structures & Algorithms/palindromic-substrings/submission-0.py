class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        for i in range(len(s)):
            L, R = i, i
            
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    counter += 1
                    R += 1
                    L -= 1
                else:
                    break
                
            L, R = i, i + 1    
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    counter += 1
                    R += 1
                    L -= 1
                else:
                    break

        return counter