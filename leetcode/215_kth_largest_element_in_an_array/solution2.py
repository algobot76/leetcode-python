class Solution:
    def findKthLargest(self, nums, k):
        if not nums:
            return -1
        return self.quick_select(nums, 0, len(nums) - 1, k)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        i = start
        j = end
        pivot = nums[(i + j) // 2]

        while i <= j:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if start + k - 1 <= j:
            return self.quick_select(nums, start, j, k)
        if start + k - 1 >= i:
            return self.quick_select(nums, i, end, k - (i - start))

        return nums[j + 1]
