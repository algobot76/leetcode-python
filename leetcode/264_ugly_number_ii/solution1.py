import heapq


class Solution:
    def nthUglyNumber(self, n):
        pq = [1]
        visited = {1}

        res = None
        for i in range(n):
            res = heapq.heappop(pq)
            for factor in [2, 3, 5]:
                num = res * factor
                if num not in visited:
                    visited.add(num)
                    heapq.heappush(pq, num)

        return res
