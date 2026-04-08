class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const indices = new Map();

        for (const [i, n] of nums.entries()) {
            indices.set(n, i);
        };

        for (const [i, n] of nums.entries()) {
            const diff = target - n;
            if (indices.has(diff) && indices.get(diff) != i) {
                return [i, indices.get(diff)];
            };
        };        
    }
}
