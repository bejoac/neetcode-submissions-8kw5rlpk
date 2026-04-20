class Solution {
public:
    int xor_sum = 0;
    vector<int> subset;
    vector<int> nums_input;

    void dfs(int i) {
        if (i == nums_input.size()) {
            int tmp = 0;
            for (int si = 0; si < subset.size(); si++) {
                tmp = tmp ^ subset[si];
            };
            xor_sum = xor_sum + tmp;
            return;
        };

        subset.push_back(nums_input[i]);
        dfs(i + 1);

        subset.pop_back();
        dfs(i + 1);
    };

    int subsetXORSum(vector<int>& nums) {
        nums_input = nums; // Wouldn't this be memory inefficient?
        dfs(0);
        return xor_sum;
    };
};