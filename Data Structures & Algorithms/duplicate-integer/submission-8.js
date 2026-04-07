class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        if (nums.length == 0) {
            return false;
        };

        const countMap = new Map();

        for (const num of nums) {
            if (countMap.has(num)) {
                return true;
            } else {
                countMap.set(num, 1);
            };
        };

        return false;
    };
};
