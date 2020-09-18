class Solution:
    def isMatch(self, s, p):
        return self.helper(s, 0, p, 0, {})

    def helper(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(s) == i:
            for idx in range(j, len(p)):
                if p[idx] != "*":
                    return False
            return True

        if len(p) == j:
            return False

        if p[j] != "*":
            matched = self.char_match(s[i], p[j]) and self.helper(s, i + 1, p,
                                                                  j + 1, memo)
        else:
            matched = self.helper(s, i + 1, p, j, memo) or self.helper(s, i, p,
                                                                       j + 1,
                                                                       memo)

        memo[(i, j)] = matched
        return matched

    def char_match(self, a, b):
        return a == b or b == "?"
