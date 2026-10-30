class Solution:
    def isPalindrome(self, n):
        if n < 0:
            return false
        og = n
        rev_no = 0

        while n > 0:
            digit = n % 10
            rev_no = rev_no * 10 + digit
            n //= 10
        return rev_no == og
       
