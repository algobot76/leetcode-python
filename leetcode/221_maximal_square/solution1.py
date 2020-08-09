class Solution:
    def maximalSquare(self, matrix):
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])

        max_len = 0
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    f[i][j] = min(f[i - 1][j], f[i][j - 1],
                                  f[i - 1][j - 1]) + 1
                    max_len = max(max_len, f[i][j])

        return max_len ** 2
