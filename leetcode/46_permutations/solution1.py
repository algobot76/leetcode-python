class Solution:
    def permute(self, nums):
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]

        nums.sort()
        ans = []
        self.dfs(nums, [], ans)
        return ans

    def dfs(self, nums, perm, ans):
        if len(nums) == 0:
            ans.append(perm)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i + 1:], perm + [nums[i]], ans)
