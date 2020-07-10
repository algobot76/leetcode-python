import collections


class Solution:
    def longestPalindrome(self, s):
        ans = 0
        cnt = collections.Counter(s)

        for i in cnt.values():
            ans += i // 2 * 2
            if ans % 2 == 0 and i % 2 == 1:
                ans += 1

        return ans
