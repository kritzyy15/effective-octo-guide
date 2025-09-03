class Solution:
    def printNum(self, ll, ul):
        if ll > ul:
            return
        print(ll)
        ll += 1
        self.printNum(ll, ul)
