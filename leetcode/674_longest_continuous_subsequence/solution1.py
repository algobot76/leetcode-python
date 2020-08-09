class Solution:
    def findLengthOfLCIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1

        ans = 0
        anchor = 0
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)

        return ans
