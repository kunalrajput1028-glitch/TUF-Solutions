class Solution:
    def reverseNumber(self, n):
        temp = abs(n)
        ams = 0
        if temp == 0:
            return 0
        while temp > 0:
            digit = temp % 10
            ams = ams * 10 + digit  
            temp //= 10
            
        return ams
n = 4456
sol = Solution()
sol.reverseNumber(n)
