import sys


class Solution:
    def maxSubArray(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        mid = (left + right) // 2
        left_sum = self.helper(nums, left, mid)
        right_sum = self.helper(nums, mid + 1, right)
        cross_sum = self.get_cross_sum(nums, left, right, mid)

        return max(left_sum, right_sum, cross_sum)

    def get_cross_sum(self, nums, left, right, mid):
        if left == right:
            return nums[left]

        left_subsum = -sys.maxsize - 1
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = -sys.maxsize - 1
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum
