class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        let max = nums[0];
        const map = {};

        for (const num of nums) {
            if (num in map) {
                map[num]++;
            } else {
                map[num] = 1;
            };

            if (map[num] > map[max]) {
                max = num;
            };
        };

        return parseInt(max);
    };
};
