class Solution:
    def climbStairs(self, n):
        f = [0, 1, 2]
        for i in range(3, n + 1):
            f[i % 3] = f[(i - 2) % 3] + f[(i - 1) % 3]
        return f[n % 3]
