class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        curr_min = nums[0]
        curr_max = nums[0]
        global_max = curr_max
        for i in range(1, n):
            num = nums[i]
            temp_max = max(num, curr_max * num, curr_min * num)
            curr_min = min(num, curr_max * num, curr_min * num)
            curr_max = temp_max
            global_max = max(global_max, curr_max)

        return global_max
