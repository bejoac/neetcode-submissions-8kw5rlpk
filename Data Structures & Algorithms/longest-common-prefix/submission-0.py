class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 201

        for st in strs: # O(n)
            min_length = min(min_length, len(st))

        i = 0
        while i < min_length: # O(n)
            cur = strs[0][i]

            for st in strs: 
                if st[i] != cur:
                    return st[:i]

            i += 1

        return strs[0][:i]