import math

class Solution:
    def divisors(self, n: int):
        n = abs(n)  
        factors = []
        sq_root_num = int(math.sqrt(n))
        
        for i in range(1, sq_root_num + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:  # avoid duplicates for perfect squares
                    factors.append(n // i)
        
        return sorted(factors)
