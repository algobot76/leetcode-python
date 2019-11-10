class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        combs = []
        self.dfs(candidates, target, 0, [], combs)
        return combs

    def dfs(self, candidates, target, start, comb, combs):
        if target < 0:
            return
        if target == 0:
            return combs.append(list(comb))

        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, comb, combs)
            comb.pop()
