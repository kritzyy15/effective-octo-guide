class Solution:
    def factorial(self, n: int) -> int:
        if n == 1:
            return 1
        return n * self.factorial(n - 1)