import collections
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1

        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            ans.append(num)

        return ans
