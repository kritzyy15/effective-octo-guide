class Solution:
    def printSum(self, n) ->  int:
        if n == 0:
            return 0
        return self.printSum(n-1) + n