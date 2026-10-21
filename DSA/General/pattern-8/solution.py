class Solution:
    def pattern8(self, n):
        for i in range(n):
            #for j in range(n,0,-1):
            print(" " * i, end="")
            print("*" * (2*(n-i)-1))

            
        