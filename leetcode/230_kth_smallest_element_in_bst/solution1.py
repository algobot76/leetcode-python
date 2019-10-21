# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

from leetcode.utils import TreeNode


class Solution:
    def kthSmallest(self, root, k):
        dummy = TreeNode(0)
        dummy.right = root
        stack = deque([dummy])

        for i in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if not stack:
                return None

        return stack.pop().val
