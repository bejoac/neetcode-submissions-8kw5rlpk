class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1

        while carry and i >= 0:
            digits[i] = digits[i] + carry
            
            if digits[i] == 10:
                digits[i] = 0
                carry = 1

                if i == 0:
                    digits.insert(0, carry)    
            else:
                carry = 0
            
            i = i - 1

        return digits