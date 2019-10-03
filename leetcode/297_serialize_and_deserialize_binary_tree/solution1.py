# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

from leetcode.utils import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''

        queue = deque([root])
        order = []
        while queue:
            node = queue.popleft()
            order.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ' '.join(order)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        order = [TreeNode(int(val)) if val != '#' else None for val in
                 data.split()]
        root = order[0]
        fast_index = 1
        nodes = [root]
        slow_index = 0
        while slow_index < len(nodes):
            node = nodes[slow_index]
            slow_index += 1
            node.left = order[fast_index]
            node.right = order[fast_index + 1]
            fast_index += 2

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return root
