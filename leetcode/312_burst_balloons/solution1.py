class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        if not n:
            return 0

        balloons = [1] + nums + [1]

        n += 2
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            f[i][i - 1] = 0

        for len_ in range(3, n + 1):
            for i in range(n - len_ + 1):
                j = i + len_ - 1
                f[i][j] = 0
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j],
                                  f[i][k] + f[k][j] + balloons[i] * balloons[
                                      k] * balloons[j])
        return f[0][n - 1]
