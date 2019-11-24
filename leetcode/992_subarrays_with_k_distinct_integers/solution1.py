import collections
from typing import List


class Window:
    def __init__(self):
        self.counts = collections.defaultdict(int)

    def add(self, num: int) -> None:
        self.counts[num] += 1

    def remove(self, num: int) -> None:
        self.counts[num] -= 1
        if self.counts[num] == 0:
            self.counts.pop(num)

    @property
    def size(self) -> int:
        return len(self.counts)


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        w1 = Window()
        w2 = Window()
        l1 = 0
        l2 = 0
        ans = 0

        for num in A:
            w1.add(num)
            while w1.size > K:
                w1.remove(A[l1])
                l1 += 1
            w2.add(num)
            while w2.size >= K:
                w2.remove(A[l2])
                l2 += 1
            ans += l2 - l1

        return ans
