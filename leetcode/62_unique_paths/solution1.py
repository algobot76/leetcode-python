class Solution:
    def uniquePaths(self, m, n):
        f = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[i][j] = 1
                if i > 0:
                    f[i][j] += f[i - 1][j]
                if j > 0:
                    f[i][j] += f[i][j - 1]

        return f[m - 1][n - 1]
