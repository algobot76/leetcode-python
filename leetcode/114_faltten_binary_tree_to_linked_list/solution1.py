# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.last_node = None

    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        if self.last_node:
            self.last_node.left = None
            self.last_node.right = root

        self.last_node = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
