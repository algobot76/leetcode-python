import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        days = -1
        if not grid or len(grid) == 0:
            return -1

        m, n = len(grid), len(grid[0])
        fresh = 0
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0:
            return 0

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for di, dj in dirs:
                    next_i, next_j = i + di, j + dj
                    if not (0 <= next_i < m and 0 <= next_j < n):
                        continue
                    if grid[next_i][next_j] == 1:
                        fresh -= 1
                        grid[next_i][next_j] = 2
                        q.append((next_i, next_j))
            days += 1

        return days if fresh == 0 else -1
