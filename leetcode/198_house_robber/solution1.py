class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev_sum = 0
        curr_sum = 0
        for num in nums:
            temp = curr_sum
            curr_sum = max(prev_sum + num, curr_sum)
            prev_sum = temp

        return curr_sum
