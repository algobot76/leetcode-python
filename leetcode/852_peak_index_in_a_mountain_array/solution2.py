class Solution:
    def peakIndexInMountainArray(self, A):
        if not A:
            return -1

        prev = A[0]
        for i in range(len(A)):
            if A[i] < prev:
                return i - 1
            prev = A[i]
