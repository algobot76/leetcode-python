class Solution:
    def findClosestElements(self, arr, k, x):
        right = self.find_upper_closest(arr, x)
        left = right - 1

        result = []
        for _ in range(k):
            if self.is_left_closer(arr, x, left, right):
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1

        result.sort()
        return result

    def find_upper_closest(self, arr, x):
        start = 0
        end = len(arr) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if arr[mid] >= x:
                end = mid
            else:
                start = mid

        if arr[start] >= x:
            return start
        if arr[end] >= x:
            return end

        return len(arr)

    def is_left_closer(self, arr, x, left, right):
        if left < 0:
            return False
        if right >= len(arr):
            return True
        return x - arr[left] <= arr[right] - x
