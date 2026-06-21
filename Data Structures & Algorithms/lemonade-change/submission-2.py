class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash_register = [0, 0, 0]


        for bill in bills:
            if bill == 5:
                cash_register[0] += 1
            elif bill == 10:
                cash_register[1] += 1
            else:
                cash_register[2] += 1

            change = bill - 5

            while change:
                if change >= 20 and cash_register[2]:
                    change -= 20
                    cash_register[2] -= 1
                elif change >= 10 and cash_register[1]:
                    change -= 10
                    cash_register[1] -= 1
                elif change >= 5 and cash_register[0]:
                    change -= 5
                    cash_register[0] -= 1
                else:
                    return False

        return True