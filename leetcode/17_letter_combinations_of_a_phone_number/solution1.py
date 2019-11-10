MAPPING = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        ans = []
        self.dfs(digits, 0, '', ans)
        return ans

    def dfs(self, digits, idx, comb, ans):
        if idx == len(digits):
            ans.append(comb)
            return

        for letter in MAPPING[digits[idx]]:
            self.dfs(digits, idx + 1, comb + letter, ans)
