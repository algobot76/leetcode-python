class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        f = [0] * n
        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])
        for i in range(2, n):
            f[i] = max(f[i - 2] + nums[i], f[i - 1])

        return f[n - 1]
