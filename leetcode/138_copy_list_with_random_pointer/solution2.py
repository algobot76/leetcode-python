"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
from leetcode.utils import Node


class Solution:
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        curr = head
        while curr is not None:
            next_ = curr.next
            curr.next = Node(curr.val, None, None)
            curr.next.next = next_
            curr = next_

        curr = head
        while curr is not None:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        dummy = Node(0, None, None)
        tail = dummy
        while curr is not None:
            next_ = curr.next.next
            clone = curr.next
            tail.next = clone
            tail = clone
            curr.next = next_
            curr = next_

        return dummy.next
