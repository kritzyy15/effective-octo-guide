from .gcd import Solution as gcdSol
class Solution:
    def LCM(self, n1, n2):
        g = gcdSol()
        return abs(n1 * n2) // g.GCD(n1, n2) if n1 and n2 else 0