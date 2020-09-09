# TLE
import sys


class Solution:
    def __init__(self):
        self.min_ = sys.maxsize

    def minimumTotal(self, triangle):
        self.dfs(triangle, 0, 0, 0)
        return self.min_

    def dfs(self, triangle, x, y, path_sum):
        if x == len(triangle):
            self.min_ = min(self.min_, path_sum)
            return

        self.dfs(triangle, x + 1, y, path_sum + triangle[x][y])
        self.dfs(triangle, x + 1, y + 1, path_sum + triangle[x][y])
