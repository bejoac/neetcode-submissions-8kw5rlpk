class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        const n = nums.length;
        const bit = Array(32).fill(0);
        for (let num of nums) {
            for (let i = 0; i < 32; i++) {
                bit[i] += (num >> i) & 1;
            }
        }

        let res = 0;
        for (let i = 0; i < 32; i++) {
            if (bit[i] > Math.floor(n / 2)) {
                res |= 1 << i;
            }
        }
        return res;
    }
}