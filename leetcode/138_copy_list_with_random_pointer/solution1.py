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

        clone_map = {}
        curr = head
        while curr is not None:
            clone_map[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        while curr is not None:
            if curr.next:
                clone_map[curr].next = clone_map[curr.next]
            if curr.random:
                clone_map[curr].random = clone_map[curr.random]
            curr = curr.next

        return clone_map[head]
