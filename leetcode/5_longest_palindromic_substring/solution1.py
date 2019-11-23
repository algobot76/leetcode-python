class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        end = 0

        for i in range(n):
            if i + (end - start) // 2 > n:
                break
            l = max(self.get_len(s, i, i), self.get_len(s, i, i + 1))
            if l > end - start:
                start = i - (l - 1) // 2
                end = start + l

        return s[start:end]

    def get_len(self, s: str, left: int, right: int) -> int:
        n = len(s)

        if right >= n or s[left] != s[right]:
            return 1

        while left >= 0 and right <= n - 1 and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
