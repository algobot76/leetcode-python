class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix[0]) == 0:
            return False

        for row in matrix:
            if target <= row[-1]:
                if not self.binary_search(row, target):
                    continue
                else:
                    return True

        return False

    def binary_search(self, row, target):
        start = 0
        end = len(row) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if row[mid] < target:
                start = mid
            elif row[mid] == target:
                end = mid
            else:
                end = mid

        return row[start] == target or row[end] == target
