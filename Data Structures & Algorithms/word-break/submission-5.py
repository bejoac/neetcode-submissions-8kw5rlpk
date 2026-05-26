class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for word in wordDict:
                end = i + len(word)
                if s[i:end] == word:  # does word match at position i?
                    if dfs(end):      # if yes, can we break the rest?
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dfs(0)