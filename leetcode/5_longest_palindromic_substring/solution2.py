class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s

        f = [[False] * n for _ in range(n)]
        ans = ""
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if self._get_len(i, j) > 2:
                        if f[i + 1][j - 1]:
                            f[i][j] = True
                    else:
                        f[i][j] = True
                if f[i][j]:
                    if self._get_len(i, j) > len(ans):
                        ans = s[i:j + 1]

        return ans

    def _get_len(self, i, j):
        return j - i + 1
