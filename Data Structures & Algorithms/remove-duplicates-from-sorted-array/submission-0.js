class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums) {
        let p = 0;
        let d = 1;

        while (p < nums.length) {
            while (d < nums.length && nums[d] == nums[p]) {
                nums.splice(d, 1);
            };

            p = d;
            d++;
        };

        return nums.length;
    };
};
