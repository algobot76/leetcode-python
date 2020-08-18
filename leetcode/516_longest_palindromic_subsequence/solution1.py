class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        if n <= 1:
            return n

        f = [[0] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i][j - 1], f[i + 1][j])
        return f[0][n - 1]
