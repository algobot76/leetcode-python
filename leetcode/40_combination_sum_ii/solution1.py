class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        combs = []
        self.dfs(candidates, target, 0, [], combs)
        return combs

    def dfs(self, candidates, target, start, comb, combs):
        if target < 0:
            return
        if target == 0:
            return combs.append(list(comb))

        prev = 0
        while start < len(candidates) and candidates[start] <= target:
            if prev != candidates[start]:
                comb.append(candidates[start])
                self.dfs(candidates, target - candidates[start], start + 1,
                         comb, combs)
                comb.pop()
                prev = candidates[start]
            start += 1
