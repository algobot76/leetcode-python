from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def get_distance(i: int):
            return points[i][0] ** 2 + points[i][1] ** 2

        def sort(left: int, right: int, K: int):
            if left >= right:
                return

            pivot_idx = (left + right) // 2
            points[left], points[pivot_idx] = points[pivot_idx], points[left]
            mid = partition(left, right)

            if K < mid - left + 1:
                sort(left, mid - 1, K)
            elif K > mid - left + 1:
                sort(mid + 1, right, K - (mid - left + 1))

        def partition(left: int, right: int):
            l = left
            r = right
            pivot = get_distance(l)

            while l < r:
                while l < r and get_distance(r) >= pivot:
                    r -= 1
                while l < r and get_distance(l) <= pivot:
                    l += 1
                points[l], points[r] = points[r], points[l]

            points[left], points[r] = points[r], points[left]
            return r

        sort(0, len(points) - 1, K)
        return points[:K]
