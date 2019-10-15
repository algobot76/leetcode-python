class Solution:
    def findPeakElement(self, nums):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < nums[mid - 1]:
                end = mid
            elif nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid

        if nums[start] < nums[end]:
            return end
        else:
            return start
