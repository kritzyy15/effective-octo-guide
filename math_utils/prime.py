import math

class Solution:
    def isPrime(self, n):
        n =  abs(n)

        if n < 2:
            return False
        
        sq_num = int(math.sqrt(n))
        
        for i in range(2, sq_num + 1):
            if n % i == 0:
                return False
            return True
