class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const s_sorted = s.split('').sort();
        const t_sorted = t.split('').sort();

        return JSON.stringify(s_sorted) == JSON.stringify(t_sorted);
    }
}
