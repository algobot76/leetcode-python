class Solution:
    def permute(self, nums):
        if not nums:
            return [[]]

        perms = []
        self.dfs(nums, [], set(), perms)
        return perms

    def dfs(self, nums, perm, visited, perms):
        if len(nums) == len(perm):
            perms.append(list(perm))
            return

        for num in nums:
            if num in visited:
                continue
            perm.append(num)
            visited.add(num)
            self.dfs(nums, perm, visited, perms)
            visited.remove(num)
            perm.pop()
