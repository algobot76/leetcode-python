from typing import List


class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.count = n

    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> bool:
        x_root, y_root = map(self.find, (x, y))
        if x_root == y_root:
            return False
        self.parents[min(x_root, y_root)] = max(x_root, y_root)
        self.count -= 1
        return True


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])
        uf = UnionFind(N)
        ans = 0
        for u, v, cost in connections:
            if uf.union(u, v):
                ans += cost
        return ans if uf.count == 1 else -1
