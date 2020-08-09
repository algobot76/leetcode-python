class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        max_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(nums[i], max_sum)
        return max_sum
