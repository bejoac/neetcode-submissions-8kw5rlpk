class Solution:
    def check_divident(self, divident: str, divisor: str) -> bool:
        multiple_divisor = divisor

        while len(multiple_divisor) <= len(divident):
            if multiple_divisor == divident:
                return True
            multiple_divisor += divisor

        return False

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        chars1 = []

        for char in str1:
            if char not in chars1:
                chars1.append(char)

        chars2 = []

        for char in str2:
            if char not in chars2:
                chars2.append(char)

        if chars1 != chars2:
            return ""

        smaller = min(str1, str2, key=len)
        bigger = max(str1, str2, key=len)
        
        while len(smaller) >= 0:
            if self.check_divident(bigger, smaller):
                return smaller

            old_smaller = smaller
            smaller = smaller[:-1]

            while len(smaller) > 0:
                if len(old_smaller) % len(smaller) != 0:
                    smaller = smaller[:-1]
                elif self.check_divident(old_smaller, smaller):
                    break       

        return ""