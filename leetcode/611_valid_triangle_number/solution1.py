class Solution:
    def triangleNumber(self, nums):
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        count = 0
        for i in range(n):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count
