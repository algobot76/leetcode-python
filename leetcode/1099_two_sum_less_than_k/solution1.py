from typing import List


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        max_ = -1
        left, right = 0, len(A) - 1
        while left < right:
            sum_ = A[left] + A[right]
            if sum_ < K and sum_ > max_:
                max_ = sum_
            elif sum_ > K:
                right -= 1
            else:
                left += 1
        return max_
