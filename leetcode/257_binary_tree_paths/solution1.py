# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)

        paths = []
        for path in left_paths + right_paths:
            paths.append(str(root.val) + '->' + path)
        return paths
