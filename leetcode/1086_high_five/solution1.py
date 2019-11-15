import collections
import heapq


class Solution:
    def highFive(self, items):
        students = collections.defaultdict(list)
        for item in items:
            students[item[0]].append(item[1])

        averages = []
        for id_, scores in students.items():
            top_five = sorted(scores, reverse=True)[:5]
            avg = sum(top_five) // len(top_five)
            heapq.heappush(averages, (id_, -avg))

        ans = []
        while len(averages) > 0:
            avg = heapq.heappop(averages)
            ans.append([avg[0], -avg[1]])

        return ans
