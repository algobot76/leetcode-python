# TLE


class Solution:
    def minimumTotal(self, triangle):
        return self.helper(triangle, 0, 0)

    def helper(self, triangle, x, y):
        if x == len(triangle):
            return 0

        left = self.helper(triangle, x + 1, y)
        right = self.helper(triangle, x + 1, y + 1)
        return min(left, right) + triangle[x][y]
