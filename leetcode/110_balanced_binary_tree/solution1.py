# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        balanced, _ = self.validate(root)
        return balanced

    def validate(self, root):
        if root is None:
            return True, 0

        balanced, left_height = self.validate(root.left)
        if not balanced:
            return False, 0
        balanced, right_height = self.validate(root.right)
        if not balanced:
            return False, 0
        return abs(left_height - right_height) <= 1, max(left_height,
                                                         right_height) + 1
