class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        result = 1
        
        if n > 0:
            for _ in range(n):
                result = result * x
        else:
            for _ in range(abs(n)):
                result = result / x      

        return result