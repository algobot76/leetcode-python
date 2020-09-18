class Solution:
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if len(s) == 0:
            return []

        partitions = []

        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for sp in sub_partitions:
                partitions.append(prefix + " " + sp)

        if s in wordDict:
            partitions.append(s)
        memo[s] = partitions
        return partitions
