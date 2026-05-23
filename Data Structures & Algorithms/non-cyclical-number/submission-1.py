class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def check_happiness(n):
            n = str(n)
            n_list = list(n)
            n_list = [int(n)**2 for n in n_list]
            happiness = sum(n_list)
            return happiness

        while n not in visited:
            visited.add(n)
            happiness = check_happiness(n)
            if happiness == 1:
                return True
            else:
                n = happiness
            
        
        return False
