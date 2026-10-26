class Solution:
    def pattern19(self, n):
        for i in range(1,n+1):
            print("*"*(n-i+1),end="")
            print(" "*(2*(i-1)),end="")
            print("*"*(n-i+1))
        for i in range(1,n+1):
            print("*"*i,end="")
            print(" "*(2*(n-i)),end="")
            print("*"*i)