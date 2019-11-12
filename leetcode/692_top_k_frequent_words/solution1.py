from collections import defaultdict


class Solution:
    def topKFrequent(self, words, k):
        counts = defaultdict(int)
        for word in words:
            counts[word] += 1

        ans = [word for (word, _) in
               sorted(counts.items(), key=lambda x: (-x[1], x[0]))]
        return ans[:k]
