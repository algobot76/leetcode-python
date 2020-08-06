import sys


class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[i][j] = grid[0][0]
                    continue
                f[i][j] = sys.maxsize
                if i > 0:
                    f[i][j] = min(f[i][j], f[i - 1][j] + grid[i][j])
                if j > 0:
                    f[i][j] = min(f[i][j], f[i][j - 1] + grid[i][j])

        return f[m - 1][n - 1]
