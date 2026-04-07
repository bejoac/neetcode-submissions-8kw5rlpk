class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = []

        for n in range(0, n+1):
            result.append(bin(n).count("1"))

        return result