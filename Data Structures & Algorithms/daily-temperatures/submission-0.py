class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        cur_i = 0
        result = []

        while cur_i < len(temperatures):
            found = False

            for next_i in range(cur_i + 1, len(temperatures)):
                if temperatures[next_i] > temperatures[cur_i]:
                    found = True
                    result.append(next_i - cur_i)
                    break
        
            if not found:
                result.append(0)

            cur_i = cur_i + 1

        return result
            
            
       