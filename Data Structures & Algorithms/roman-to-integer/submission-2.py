class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        
        roman_to_int = {
            "I": 1, 
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        output = 0
        i = 0

        while i < len(s):
            if s[i] == "I":
                if i + 1 < len(s) and s[i + 1] == "V":
                    output += 4
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == "X":
                    output += 9
                    i += 1
                else:
                    output += 1

            elif s[i] == "X":
                if i + 1 < len(s) and s[i + 1] == "L":
                    output += 40
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == "C":
                    output += 90
                    i += 1
                else:
                    output += 10
            
            elif s[i] == "C":
                if i + 1 < len(s) and s[i + 1] == "D":
                    output += 400
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == "M":
                    output += 900
                    i += 1
                else:
                    output += 100

            else:
                output += roman_to_int[s[i]]

            i += 1

        return output
