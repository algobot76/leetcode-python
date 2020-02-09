class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.helper(nums, 0, len(nums) - 1)
        return nums

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[left]
        i = left
        j = right

        while i < j:
            while i <= right and nums[i] <= pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j

    def helper(self, nums: List[int], left: int, right: int):
        if right > left:
            pivot_idx = self.partition(nums, left, right)
            self.helper(nums, left, pivot_idx - 1)
            self.helper(nums, pivot_idx + 1, right)
