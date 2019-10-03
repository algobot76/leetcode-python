from collections import deque


class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        return islands

    def bfs(self, grid, x, y, visited):
        q = deque([(x, y)])
        visited.add((x, y))
        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if not self.is_valid(grid, nx, ny, visited):
                    continue
                q.append((nx, ny))
                visited.add((nx, ny))

    def is_valid(self, grid, x, y, visited):
        m = len(grid)
        n = len(grid[0])
        return 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == '1'
