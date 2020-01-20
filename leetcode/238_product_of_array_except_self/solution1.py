from typing import List


# TLE
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prod(pos: int):
            result = 1
            for i in range(len(nums)):
                if i != pos:
                    result *= nums[i]
            return result

        ans = []
        for i in range(len(nums)):
            ans.append(prod(i))
        return ans
