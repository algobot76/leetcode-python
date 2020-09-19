class Solution:
    def isMatch(self, s, p):
        return self.helper(s, 0, p, 0, {})

    def helper(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(s) == i:
            return self.is_empty(p[j:])

        if len(p) == j:
            return False

        if j + 1 < len(p) and p[j+1] == "*":
            matched = self.is_matched_char(s[i], p[j]) and self.helper(
                s, i+1, p, j, memo) or self.helper(s, i, p, j+2,  memo)
        else:
            matched = self.is_matched_char(
                s[i], p[j]) and self.helper(s, i+1, p, j+1, memo)
        memo[(i, j)] = matched
        return matched

    def is_matched_char(self, s, p):
        return s == p or p == "."

    def is_empty(self, p):
        if len(p) % 2 == 1:
            return False

        for i in range(len(p) // 2):
            if p[i * 2 + 1] != "*":
                return False
        return True
