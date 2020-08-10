# TLE
class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        f = [[0] * n for _ in range(2)]
        curr_max = nums[0]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    f[i % 2][j] = nums[i]
                elif j - i + 1 == 2:
                    f[i % 2][j] = nums[i] * nums[j]
                else:
                    f[i % 2][j] = f[(i + 1) % 2][j - 1] * nums[i] * nums[j]
                curr_max = max(curr_max, f[i % 2][j])

        return curr_max
