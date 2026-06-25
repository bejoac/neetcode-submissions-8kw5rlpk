class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""

        # This can probably be solved more elegantly
        if len(a) > len(b):
            while len(a) > len(b):
                b = "0" + b

        if len(a) < len(b):
            while len(a) < len(b):
                a = "0" + a

        carry = 0

        for i in range(len(a) - 1, -1, -1):
            if int(a[i]) ^ int(b[i]):
                if carry:
                    ans = "0" + ans
                else:
                    ans = "1" + ans
            
            elif int(a[i]) & int(b[i]):
                if carry:
                    ans = "1" + ans
                else:
                    ans = "0" + ans
                    carry = 1
            
            else:
                if carry:
                    ans = "1" + ans
                    carry = 0
                else:
                    ans = "0" + ans

        if carry:
            ans = "1" + ans

        return ans