class Solution:
    def partitionLabels(self, S):
        last_indices = {ch: i for i, ch in enumerate(S)}
        left = 0
        right = 0
        ans = []

        for i, ch in enumerate(S):
            right = max(right, last_indices[ch])
            if i == right:
                ans.append(right - left + 1)
                left = right + 1

        return ans
