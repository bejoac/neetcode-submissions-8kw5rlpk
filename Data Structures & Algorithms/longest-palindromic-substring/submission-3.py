class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrom = ""

        for i in range(len(s)):
            L, R = i, i
            
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if len(s[L:R+1]) > len(palindrom):
                        palindrom = s[L:R+1]
                    R += 1
                    L -= 1
                else:
                    break
                
            L, R = i, i + 1    
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    if len(s[L:R+1]) > len(palindrom):
                        palindrom = s[L:R+1]
                    R += 1
                    L -= 1
                else:
                    break

        return palindrom
            