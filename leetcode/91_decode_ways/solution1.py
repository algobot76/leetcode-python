class Solution:
    def numDecodings(self, s):
        if not s or s[0] == "0":
            return 0

        n = len(s)
        f = [1, 0, 0]
        f[1] = self.num_ways(s[0])

        for i in range(2, n + 1):
            f[i % 3] = f[(i - 1) % 3] * self.num_ways(s[i - 1:i]) + f[
                (i - 2) % 3] * self.num_ways(s[i - 2:i])

        return f[n % 3]

    def num_ways(self, s):
        code = int(s)
        if len(s) == 1 and 1 <= code <= 9:
            return 1
        if len(s) == 2 and 10 <= code <= 26:
            return 1

        return 0
