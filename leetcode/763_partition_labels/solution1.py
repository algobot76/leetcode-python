class Solution:
    def partitionLabels(self, S):
        left = 0
        right = 0
        ans = []
        for i in range(len(S)):
            right = max(right, S.rfind(S[i]))
            if i == right:
                ans.append(right - left + 1)
                left = right + 1

        return ans
