class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    validPalindrome(s) {
        function isPalin(l, r) {
            while (l < r) {
                if (s[l] != s[r]) {
                    return false;
                };
                l++;
                r--;
            };

            return true;
        };

        let l = 0;
        let r = s.length - 1;

        while (l < r) {
            if (s[l] != s[r]) {
                return (isPalin(l + 1, r) || isPalin(l, r - 1));
            };
            r--;
            l++;
        };

        return true;
    };
};
