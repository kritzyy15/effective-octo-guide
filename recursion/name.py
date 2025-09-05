class Solution:
    def printName(self, ll, ul):
        if ll > ul:
            return
        print("I am Iron Man")
        self.printName(ll + 1, ul)
