# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.utils import TreeNode


class Solution:
    def __init__(self):
        self.max_avg = 0

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.postorder(root)
        return self.max_avg

    def postorder(self, root) -> (int, int):
        if not root:
            return 0, 0

        left_total, left_size = self.postorder(root.left)
        right_total, right_size = self.postorder(root.right)
        total = left_total + right_total + root.val
        size = left_size + right_size + 1
        self.max_avg = max(self.max_avg, total / size)
        return total, size
