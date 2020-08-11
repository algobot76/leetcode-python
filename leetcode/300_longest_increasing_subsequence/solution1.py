class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        f = [0] * n
        f[0] = 1
        global_max = f[0]
        for i in range(1, n):
            max_len = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_len = max(max_len, f[j])
            f[i] = max_len + 1
            global_max = max(global_max, f[i])
        return global_max
