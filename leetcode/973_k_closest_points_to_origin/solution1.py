import heapq

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = self.get_distance(point)
            heapq.heappush(heap, (-dist, -point[0], -point[1]))
            if len(heap) > K:
                heapq.heappop(heap)

        ans = []
        while len(heap) > 0:
            (_, x, y) = heapq.heappop(heap)
            ans.append([-x, -y])
        return ans

    def get_distance(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        return x ** 2 + y ** 2
