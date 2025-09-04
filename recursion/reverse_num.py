class Solution:
    def printNumReverse(self, ul, ll):
        print(ul)
        if ul == ll:
            return
        ul -= 1
        self.printNumReverse(ul, ll)