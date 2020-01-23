import collections
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        old = image[sr][sc]
        if old == newColor:
            return image

        rows = len(image)
        cols = len(image[0])

        q = collections.deque([(sr, sc)])
        visited = set()
        while q:
            (r, c) = q.popleft()
            if image[r][c] == old:
                image[r][c] = newColor
                visited.add((r, c))

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if self.is_valid(rows, cols, visited, nr, nc):
                        q.append((nr, nc))

        return image

    def is_valid(self, rows: int, cols: int, visited: set, r: int, c: int):
        return 0 <= r < rows and 0 <= c < cols and (r, c) not in visited
