class Solution:
    def solveNQueens(self, n):
        ans = []
        self.dfs(n, [], [], [], ans)
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in result] for result
                in ans]

    def dfs(self, n, col_per_row, xy_diff, xy_sum, ans):
        cur_row = len(col_per_row)
        if cur_row == n:
            ans.append(col_per_row)
        for col in range(n):
            if col not in col_per_row and (cur_row - col not in xy_diff) and (
                    cur_row + col not in xy_sum):
                self.dfs(n, col_per_row + [col], xy_diff + [cur_row - col],
                         xy_sum + [cur_row + col], ans)
