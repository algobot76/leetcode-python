class Solution:
    def climbStairs(self, n):
        f = [0] * (n + 1)
        return self.helper(0, n, f)

    def helper(self, i, n, f):
        if i > n:
            return 0
        if i == n:
            return 1
        if f[i] > 0:
            return f[i]

        f[i] = self.helper(i + 1, n, f) + self.helper(i + 2, n, f)
        return f[i]
