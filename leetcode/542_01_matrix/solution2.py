from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[100_000 for _ in range(n)] for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    dp[x][y] = 0
                if x > 0:
                    dp[x][y] = min(dp[x][y], dp[x - 1][y] + 1)
                if y > 0:
                    dp[x][y] = min(dp[x][y], dp[x][y - 1] + 1)
        for x in range(m - 1, -1, -1):
            for y in range(n - 1, -1, -1):
                if dp[x][y] > 0:
                    if x < m - 1:
                        dp[x][y] = min(dp[x][y], dp[x + 1][y] + 1)
                    if y < n - 1:
                        dp[x][y] = min(dp[x][y], dp[x][y + 1] + 1)
        return dp
