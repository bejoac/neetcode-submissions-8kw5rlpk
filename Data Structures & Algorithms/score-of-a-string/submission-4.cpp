class Solution {
public:
    int scoreOfString(string s) {
        int score = 0;

        for (int i; i < s.length() - 1; i++) {
            score = score + abs(s[i] - s[i + 1]);
        };

        return score;
    };
};