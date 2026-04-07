class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        self.count = 0

        def dfs(cur_sum):
            if cur_sum == n:
                self.count += 1
                return
            elif cur_sum > n:
                return
            
            dfs(cur_sum + 1)  # Take 1 step
            dfs(cur_sum + 2)  # Take 2 steps

        dfs(0)
        return self.count
        