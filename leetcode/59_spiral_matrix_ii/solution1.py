from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans, lo = [], n * n + 1
        while lo > 1:
            lo, hi = lo - len(ans), lo
            ans = [range(lo, hi)] + list(zip(*ans[::-1]))
        return ans
