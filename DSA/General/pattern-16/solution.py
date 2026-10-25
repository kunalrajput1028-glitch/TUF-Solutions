class Solution:
    def pattern16(self, n):
        for i in range(1,n+1):
            ch = chr(ord('A')+i-1)
            print(ch * i)
        