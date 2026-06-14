class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    searchInsert(nums, target) {
        // if (target > nums[nums.length - 1]) return nums.length;
        // if (target < nums[0]) return 0;

        let L = 0;
        let R = nums.length - 1
        let M;

        while (L <= R) {
            M = Math.floor(L + (R - L) / 2);

            if (nums[M] < target) {
                L = M + 1;
            } else if (nums[M] == target) {
                return M;
            } else {
                R = M - 1
            };
        };  

        return L;
    };
};
