import heapq
from typing import List


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m = len(A)
        n = len(A[0])
        heap = [(-A[0][0], 0, 0)]
        visited = {(0, 0)}
        while heap:
            i, r, c = heapq.heappop(heap)
            if r == len(A) - 1 and c == len(A[0]) - 1:
                return -i
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(heap, (-min(-i, A[nr][nc]), nr, nc))
                    visited.add((nr, nc))
        return -1
