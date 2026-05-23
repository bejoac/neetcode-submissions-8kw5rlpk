class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        result = 1
        
        for _ in range(abs(n)):
            result = result * x

        if n > 0:
            return result
        else:
            return 1 / result