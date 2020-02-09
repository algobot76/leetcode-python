class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            if self.is_valid(s, l, r - 1) or self.is_valid(s, l + 1, r):
                return True
            else:
                return False

        return True

    def is_valid(self, s: str, left: int, right: int) -> bool:
        l = left
        r = right

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
