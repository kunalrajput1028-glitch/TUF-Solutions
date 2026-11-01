class Solution:
    def isPerfect(self, n: int) -> bool:
        if n <= 1:
            return False 
        div_sum = 0
        for i in range(1,(n//2)+1):
            if n % i == 0:
                div_sum += i
        return div_sum == n