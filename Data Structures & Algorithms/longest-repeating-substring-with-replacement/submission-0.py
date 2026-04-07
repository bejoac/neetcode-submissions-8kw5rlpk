from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0, 1

        result = 0

        while L < len(s) - 1:
            counter = Counter(s[L:R])
            max_count = max(counter.values())
            total_count = sum(counter.values())

            if (total_count - max_count) <= k:
              result = max(result, total_count)

            if (total_count - max_count) <= k and R < len(s):
                R = R + 1
            else:
                L = L + 1

        return result
    
