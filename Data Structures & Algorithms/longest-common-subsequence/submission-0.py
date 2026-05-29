class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for col in range(len(text1) + 1)] for row in range((len(text2) + 1))]

        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                if text2[i] == text1[j]:
                    memo[i][j] = 1 + memo[i + 1][j + 1]
                else:
                    memo[i][j] = max(memo[i + 1][j], memo[i][j + 1])

        return memo[0][0]