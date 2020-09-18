class Solution:
    def minimumTotal(self, triangle):
        return self.helper(triangle, 0, 0, {})

    def helper(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0
        if (x, y) in memo:
            return memo[(x, y)]

        left = self.helper(triangle, x + 1, y, memo)
        right = self.helper(triangle, x + 1, y + 1, memo)

        memo[(x, y)] = min(left, right) + triangle[x][y]
        return memo[(x, y)]
