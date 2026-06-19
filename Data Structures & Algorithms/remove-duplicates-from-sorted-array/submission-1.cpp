class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int p = 0;
        int d = 1;

        while (p < nums.size()) {
            while (d < nums.size() && nums[d] == nums[p]) {
                nums.erase(nums.begin() + d);
            };

            p = d;
            d++;
        };

        return nums.size();
    };
};