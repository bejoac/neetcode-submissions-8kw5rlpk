class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def check_happiness(n):
            happiness = 0

            while n:
                digit = n % 10
                digit = digit ** 2
                happiness = happiness + digit
                n = n // 10
            
            return happiness

        while n not in visited:
            visited.add(n)
            happiness = check_happiness(n)
            
            if happiness == 1:
                return True
            else:
                n = happiness
            
        return False
