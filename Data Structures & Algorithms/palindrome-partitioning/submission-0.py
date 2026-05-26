class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False

        return True

    def partition(self, s: str) -> List[List[str]]:
        palindrome = []
        palindromes = []

        def dfs(i):
            if i >= len(s):
                palindromes.append(palindrome.copy())
                return

            for j in range(i, len(s)):
                if self.is_palindrome(s[i:j+1]):
                    palindrome.append(s[i:j+1])
                    dfs(j + 1)
                    palindrome.pop()

        dfs(0)
        return palindromes

            