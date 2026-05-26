class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
            
        num_to_char = {}

        num_to_char["2"] = ["a", "b", "c"]
        num_to_char["3"] = ["d", "e", "f"]
        num_to_char["4"] = ["g", "h", "i"]
        num_to_char["5"] = ["j", "k", "l"]
        num_to_char["6"] = ["m", "n", "o"]
        num_to_char["7"] = ["p", "q", "r", "s"]
        num_to_char["8"] = ["t", "u", "v"]
        num_to_char["9"] = ["w", "x", "y", "z"]

        output = []
        res = []

        def dfs(i):
            if i >= len(digits):
                str_res = "".join(res)
                output.append(str_res)
                return 

            for char in num_to_char[digits[i]]:
                res.append(char)
                dfs(i + 1)
                res.pop()

        dfs(0)
        return output