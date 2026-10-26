class Solution:
    def pattern22(self, n):
        size = 2*n-1
        for i in range(size):
            for j in range(size):
                bottom = size-1-i
                right = size-1-j
                if i<=j and i<=bottom and i<=right:
                    m = i
                elif j<=bottom and j<= right:
                    m = j
                elif bottom <= right:
                    m = bottom
                else:
                    m = right
                val = n-m
                print(val,end=" ")
            print()
                