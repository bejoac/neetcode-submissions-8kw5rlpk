class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        
        int rows = text1.size();
        int cols = text2.size();
        
        vector<vector<int>> memo(rows + 1, vector<int>(cols + 1, 0));
        
        for (int i = rows - 1; i >= 0; i--) {
            for (int j = cols - 1; j >= 0; j--) {
                if (text1[i] == text2[j]) {
                    memo[i][j] = 1 + memo[i + 1][j + 1];
                } else {
                    memo[i][j] = max(memo[i + 1][j], memo[i][j + 1]);
                };
            };
        };
        return memo[0][0];
    };
};