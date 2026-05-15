#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        int l = 0;
        vector<char> sub_array;

        for (int r = 0; r < s.size(); r++) {
            while (std::find(sub_array.begin(), sub_array.end(), s[r]) != sub_array.end()) {
                std::erase(sub_array, s[l]);
                l++;
            };
            sub_array.push_back(s[r]);
            res = std::max(res, (int)sub_array.size());
        };

    return res;
    
    };
};
