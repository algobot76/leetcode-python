import collections
import sys
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        q = collections.deque()
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    q.append((x, y))
                else:
                    matrix[x][y] = sys.maxsize

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            cell = q.popleft()
            x, y = cell
            for dir in dirs:
                nx = x + dir[0]
                ny = y + dir[1]
                if not (0 <= nx < m) or not (0 <= nx < n) or (
                        matrix[nx][ny] <= matrix[x][y] + 1):
                    continue
                q.append((nx, ny))
                matrix[nx][ny] = matrix[x][y] + 1

        return matrix
