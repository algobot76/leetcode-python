# TLE
class Solution:
    def climbStairs(self, n):
        return self.helper(0, n)

    def helper(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1

        return self.helper(i + 1, n) + self.helper(i + 2, n)
