from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        self.sort(points, 0, len(points) - 1, K)
        return points[:K]

    def sort(self, points: List[List[int]], left: int, right: int, K: int):
        if left >= right:
            return

        pivot_idx = self.partition(points, left, right)

        if K < pivot_idx - left + 1:
            self.sort(points, left, pivot_idx - 1, K)
        elif K > pivot_idx - left + 1:
            self.sort(points, pivot_idx + 1, right, K - (pivot_idx - left + 1))

    def partition(self, points: List[List[int]], left: int, right: int):
        pivot = self.get_dist(points, left)
        i = left
        j = right

        while i < j:
            while i <= right and self.get_dist(points, i) <= pivot:
                i += 1
            while self.get_dist(points, j) > pivot:
                j -= 1
            if i < j:
                points[i], points[j] = points[j], points[i]

        points[left], points[j] = points[j], points[left]
        return j

    def get_dist(self, points: List[List[int]], i: int) -> int:
        return points[i][0] ** 2 + points[i][1] ** 2
