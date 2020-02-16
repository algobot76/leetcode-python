class Solution:
    def __init__(self):
        self.ans = []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.two_sum(nums, i + 1, len(nums) - 1, -nums[i])
        return self.ans

    def two_sum(self, nums: List[int], left: int, right: int, target: int):
        while left < right:
            if nums[left] + nums[right] == target:
                self.ans.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
