class Solution:
    def countDigit(self, n):
        if n==0:
            return 1
        count = 0
        temp = n 
        while temp > 0:
            count += 1
            temp //= 10
        return(count)