# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappush, heappop

from leetcode.utils import ListNode

ListNode.__lt__ = lambda x, y: (x.val < y.val)


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        dummy = ListNode(0)
        curr = dummy

        pq = []
        for node in lists:
            if node:
                heappush(pq, node)

        while pq:
            min_ = heappop(pq)
            curr.next = min_
            curr = curr.next
            if min_.next:
                heappush(pq, min_.next)

        return dummy.next
