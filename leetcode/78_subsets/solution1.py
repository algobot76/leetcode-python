class Solution:
    def subsets(self, nums):
        nums.sort()
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets

    def dfs(self, nums, idx, subset, subsets):
        subsets.append(list(subset))
        for i in range(idx, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()
