class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const nums_obj = {};
        
        for (const num of nums) {
            if (num.toString() in nums_obj) {
                return true;
            } else {
                nums_obj[num.toString()] = 1;
            }
        }

        return false;
    }
}
