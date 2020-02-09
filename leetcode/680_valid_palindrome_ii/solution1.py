# TLE
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            temp = s[0:i] + s[i + 1:]
            if self.is_valid(temp):
                return True

        return False

    def is_valid(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
