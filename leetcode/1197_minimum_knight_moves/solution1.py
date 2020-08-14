import collections

MOVES = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2),
         (-2, -1)]


class Solution:
    def minKnightMoves(self, x, y):
        if x == 0 and y == 0:
            return 0

        q = collections.deque([(0, 0, 0)])
        visited = {(0, 0)}
        while q:
            cx, cy, steps = q.popleft()
            if cx == x and cy == y:
                return steps
            for dx, dy in MOVES:
                nx = cx + dx
                ny = cy + dy
                if (nx, ny) not in visited:
                    if nx == x and ny == y:
                        return steps + 1
                    q.append((nx, ny, steps + 1))
                    visited.add((nx, ny))
