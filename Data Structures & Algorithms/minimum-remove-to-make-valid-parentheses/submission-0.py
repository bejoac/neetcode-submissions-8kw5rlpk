class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        i = 0
        s = list(s)
        stack = []

        while i < len(s):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")" and stack:
                stack.pop()
            elif s[i] == ")" and not stack:
                s[i] = ''
    
            i = i + 1
        
        if stack:
            for i in stack:
                s[i] = ''

        return ''.join(s)