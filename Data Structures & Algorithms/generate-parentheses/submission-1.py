class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def check_valid(subres):
            stack = []
            subres = [c for c in subres]

            for element in subres:
                if element == "(":
                    stack.append(element)
                elif element == ")" and stack:
                    stack.pop()
                elif element == ")" and not stack:
                    return False
            
            if stack: 
                return False
            
            return True

        res = []

        def dfs(subres):
            len_subres = len([c for c in subres])
            # Base case:

            if len_subres // 2 == n:
                valid = check_valid(subres)
                if valid:
                    res.append(subres)
                    return
                if not valid:
                    return

            # Recursive case
            dfs(subres + "(")
            dfs(subres + ")")

        dfs(subres="(")

        return res