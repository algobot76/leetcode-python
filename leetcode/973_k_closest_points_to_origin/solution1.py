import heapq


class Solution:
    def kClosest(self, points, K):
        pq = []
        for point in points:
            dist = self.get_distance(point)
            heapq.heappush(pq, (-dist, -point[0], -point[1]))
            if len(pq) > K:
                heapq.heappop(pq)

        ans = []
        while len(pq) > 0:
            (_, x, y) = heapq.heappop(pq)
            ans.append([-x, -y])
        return ans

    def get_distance(self, point):
        x = point[0]
        y = point[1]
        return x ** 2 + y ** 2
