class Solution:
    def countOddDigit(self, n): 
        count = 0
        temp = abs(n)
        if temp == 0:
            return 0
        while temp > 0:
            digit = temp % 10
            if digit % 2 != 0:
                count += 1
            temp //= 10
        return count