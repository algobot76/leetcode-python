from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int,
                  newColor: int) -> List[List[int]]:
        old = image[sr][sc]
        if old == newColor:
            return image
        self.dfs(image, old, newColor, sr, sc)
        return image

    def dfs(self, image: List[List[int]], old: int, new: int, r: int, c: int):
        rows = len(image)
        cols = len(image[0])

        if image[r][c] == old:
            image[r][c] = new
            if r >= 1:
                self.dfs(image, old, new, r - 1, c)
            if r + 1 < rows:
                self.dfs(image, old, new, r + 1, c)
            if c >= 1:
                self.dfs(image, old, new, r, c - 1)
            if c + 1 < cols:
                self.dfs(image, old, new, r, c + 1)
