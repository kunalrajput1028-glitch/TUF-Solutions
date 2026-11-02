class Solution:
    def primeUptoN(self, n):
        temp = n
        count = 0 
        if temp == 0:
            return False
        for i in range(2,n+1):
            is_prime = True
            for j in range(2,i):
                if i % j == 0:
                    is_prime = False
            if is_prime == True:
                count += 1
        return count