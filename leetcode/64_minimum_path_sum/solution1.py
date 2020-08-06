import sys


class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        f = [[0] * n for _ in range(2)]

        curr = 0

        for i in range(m):
            prev = curr
            curr = 1 - curr
            for j in range(n):
                if i == 0 and j == 0:
                    f[curr][j] = grid[0][0]
                    continue
                f[curr][j] = sys.maxsize
                if i > 0:
                    f[curr][j] = min(f[curr][j], f[prev][j] + grid[curr][j])
                if j > 0:
                    f[curr][j] = min(f[curr][j], f[curr][j - 1] + grid[i][j])

        return f[curr][n - 1]
