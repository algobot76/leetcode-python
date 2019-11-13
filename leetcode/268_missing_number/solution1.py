import collections


class Solution:
    def missingNumber(self, nums):
        n = len(nums) + 1

        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1
        for i in range(n + 1):
            if counts[i] == 0:
                return i

        return -1
