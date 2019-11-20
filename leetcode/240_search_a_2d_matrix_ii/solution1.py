class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix[0]) == 0:
            return False

        for row in matrix:
            if target in row:
                return True
        return False
