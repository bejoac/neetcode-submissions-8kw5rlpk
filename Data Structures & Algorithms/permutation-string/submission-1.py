from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)

        counter_s1 = Counter(s1)

        while r <= len(s2):
            counter_s2 = Counter(s2[l:r])
            
            if counter_s2 == counter_s1:
                return True

            l = l + 1
            r = r + 1

        return False