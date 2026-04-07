class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_b = max(piles)
        min_b = 1

        while min_b <= max_b:
            time = 0
            k = (max_b + min_b) // 2

            for pile in piles:
                quotient = pile // k
                rest = pile % k

                if rest:
                    time = time + quotient + 1
                else:
                    time = time + quotient

            if time > h:
                min_b = k + 1
            elif time <= h:
                res = k
                max_b = k - 1

        return res
        
        