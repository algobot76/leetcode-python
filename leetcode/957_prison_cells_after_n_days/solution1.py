from typing import List

# TLE
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if not cells or len(cells) == 0 or N <= 0:
            return cells

        for i in range(N):
            cells = self.next_day(cells)

        return cells

    def next_day(self, cells: List[int]) -> List[int]:
        next_cells = [0 for _ in range(len(cells))]
        for i in range(1, len(cells) - 1):
            if cells[i - 1] == cells[i + 1]:
                next_cells[i] = 1
        return next_cells
