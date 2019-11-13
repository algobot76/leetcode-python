import collections

class Solution:
    def firstUniqChar(self, s):
        if not s:
            return -1

        counts = collections.defaultdict(int)
        for c in s:
            counts[c] += 1

        for idx, c in enumerate(s):
            if counts[c] == 1:
                return idx

        return -1
