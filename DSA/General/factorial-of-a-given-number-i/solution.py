class Solution:
    def factorial(self, n):
        if n < 0:
            return "factorial for a negative no. is not defined."
        result = 1
        for i in range(1,n+1):
            result *= i
        return result 