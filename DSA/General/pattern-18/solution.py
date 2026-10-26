class Solution:
    def pattern18(self, n):
        for i in range(1,n+1):
            for j in range(i):
                print(chr(ord('A')+n-i+j),end=" ")
            print()