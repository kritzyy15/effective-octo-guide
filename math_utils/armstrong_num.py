class Solution:
    def isArmstrong(self, n):
        sign = -1 if n < 0 else 1

        digits = str(n)
        power = len(digits)
        
        total = sum(int(d) ** power for d in digits) * sign

        return total == n