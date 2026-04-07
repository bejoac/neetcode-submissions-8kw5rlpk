class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(char for char in s if char.isalnum()).lower()

        L = 0 
        R = len(s) - 1

        while L < R:
            if (s[L] != s[R]):
                return False

            L += 1
            R -= 1
        
        return True