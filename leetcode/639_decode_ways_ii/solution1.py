class Solution:
    def numDecodings(self, s):
        if not s:
            return 0

        n = len(s)
        f = [1, 0, 0]
        f[1] = self.count1(s[0])

    def count1(self, s):
        if s == "*":
            return 9

        if s == "0":
            return 0
        return 1
