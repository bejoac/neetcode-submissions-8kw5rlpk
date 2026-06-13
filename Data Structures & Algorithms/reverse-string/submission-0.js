class Solution {
    /**
     * @param {character[]} s
     * @return {void} Do not return anything, modify s in-place instead.
     */
    reverseString(s) {
        let L = 0;
        let R = s.length - 1;

        while (L < R) {
            const tmp = s[L];
            s[L] = s[R];
            s[R] = tmp;

            L++;
            R--;
        };

        return s;
    };
};
