from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        temp = 1
        for i in range(len(nums)):
            ans.append(temp)
            temp *= nums[i]

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= temp
            temp *= nums[i]

        return ans
