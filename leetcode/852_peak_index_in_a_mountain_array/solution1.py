class Solution:
    def peakIndexInMountainArray(self, A):
        if not A:
            return -1

        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] > A[mid + 1]:
                end = mid
            else:
                start = mid

        return start if A[start] > A[end] else end
