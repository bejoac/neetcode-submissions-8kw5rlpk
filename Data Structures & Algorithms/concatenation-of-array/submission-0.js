class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    getConcatenation(nums) {
        const copy = [...nums];

        for (const num of copy) {
            nums.push(num);
        };

        return nums;
    };
};
