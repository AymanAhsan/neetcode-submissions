class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) return false;
        let count_s = {};
        let count_t = {};
        for (let i = 0; i < s.length; i++){
           count_s[s[i]] = (count_s[s[i]] || 0) + 1;
           count_t[t[i]] = (count_t[t[i]] || 0) + 1;
        }

        // Will check each key ie count_s[r] and count_t[r]
        for (const key in count_s) {
            if (count_s[key] !== count_t[key]) {
                return false;
            }
        }
        return true;
    }
}
