class Solution:
    def findMin(self, nums):
        if not nums:
            return -1

        min_ = nums[0]
        for num in nums:
            min_ = min(min_, num)
        return min_
