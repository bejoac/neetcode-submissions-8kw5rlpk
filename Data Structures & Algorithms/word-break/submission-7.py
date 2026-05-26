class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(i, curr):
            if s[:len(curr)] != curr:
                return False
                
            if curr == s:
                return True

            if i >= len(s):
                return False

            for j in range(0, len(wordDict)):
                if dfs(i + len(wordDict[j]), curr + wordDict[j]):
                    return True

            return False

        return dfs(0, "")